#!/usr/bin/env bash
# CP Sync — установка и обновление на VPS (Ubuntu 22.04/24.04 или Debian 12).
#
#   curl -fsSL https://raw.githubusercontent.com/Nmk102/cpsync/main/deploy/install.sh | sudo bash
#
# Повторный запуск той же команды — обновление до последней версии (данные сохраняются).
# Свой домен (DNS-запись A уже указывает на сервер):
#   curl -fsSL .../install.sh | sudo CPSYNC_DOMAIN=cpsync.example.com bash
# Закрыть регистрацию для посторонних:  ... | sudo CPSYNC_REGISTRATION=closed bash
set -euo pipefail

REPO="${CPSYNC_REPO:-Nmk102/cpsync}"
BRANCH="${CPSYNC_BRANCH:-main}"
DIR=/opt/cpsync
DATA=/var/lib/cpsync

say() { printf '\n\033[1;36m==> %s\033[0m\n' "$*"; }
die() { printf '\n\033[1;31mОшибка: %s\033[0m\n' "$*" >&2; exit 1; }

[ "$(id -u)" -eq 0 ] || die "запустите от root: добавьте sudo перед bash"
command -v curl >/dev/null || { apt-get update -qq && apt-get install -y -qq curl ca-certificates; }

# --- 1. Docker
if ! command -v docker >/dev/null 2>&1; then
  say "Устанавливаю Docker (1–2 минуты)…"
  curl -fsSL https://get.docker.com | sh >/dev/null
fi
systemctl enable --now docker >/dev/null 2>&1 || true
docker compose version >/dev/null 2>&1 || die "не найден docker compose"

# --- 2. Небольшой своп на маленьких серверах (компиляция C++ любит память)
if [ "$(free -m | awk '/^Mem:/{print $2}')" -lt 2000 ] && ! swapon --show | grep -q .; then
  say "Добавляю своп 2 ГБ…"
  fallocate -l 2G /swapfile && chmod 600 /swapfile && mkswap /swapfile >/dev/null && swapon /swapfile
  grep -q '/swapfile' /etc/fstab || echo '/swapfile none swap sw 0 0' >> /etc/fstab
fi

# --- 3. Код
say "Скачиваю CP Sync ($REPO, ветка $BRANCH)…"
TMP=$(mktemp -d)
curl -fsSL "https://codeload.github.com/$REPO/tar.gz/refs/heads/$BRANCH" | tar xz -C "$TMP" --strip-components=1 \
  || die "не удалось скачать код с GitHub"
mkdir -p "$DIR" "$DATA"
SAVED_DOMAIN=$(grep -s '^CPSYNC_DOMAIN=' "$DIR/.env" | cut -d= -f2- || true)
SAVED_REG=$(grep -s '^CPSYNC_REGISTRATION=' "$DIR/.env" | cut -d= -f2- || true)
find "$DIR" -mindepth 1 -maxdepth 1 ! -name .env -exec rm -rf {} +
cp -a "$TMP/." "$DIR/"
rm -rf "$TMP"
curl -fsS --max-time 15 -H 'Accept: application/vnd.github.sha' \
  "https://api.github.com/repos/$REPO/commits/$BRANCH" > "$DIR/.commit" 2>/dev/null || true

# --- 4. Адрес сайта
DOMAIN="${CPSYNC_DOMAIN:-$SAVED_DOMAIN}"
if [ -z "$DOMAIN" ]; then
  IP=$(curl -fsS4 --max-time 10 https://api.ipify.org || curl -fsS4 --max-time 10 https://ifconfig.me || true)
  [ -n "$IP" ] || die "не удалось узнать внешний IP — укажите домен: CPSYNC_DOMAIN=..."
  DOMAIN="${IP//./-}.sslip.io"
fi
REG="${CPSYNC_REGISTRATION:-${SAVED_REG:-open}}"
cat > "$DIR/.env" <<ENV
CPSYNC_DOMAIN=$DOMAIN
CPSYNC_REGISTRATION=$REG
ENV

# --- 5. Брандмауэр (если включён)
if command -v ufw >/dev/null 2>&1 && ufw status | grep -q 'Status: active'; then
  ufw allow 80/tcp >/dev/null; ufw allow 443/tcp >/dev/null; ufw allow 443/udp >/dev/null
fi

# --- 6. Сборка и запуск
say "Собираю песочницу для запуска кода (компиляторы C/C++ и Python)…"
docker build -q -t cpsync-sandbox:latest "$DIR/server/sandbox" >/dev/null
say "Запускаю CP Sync…"
cd "$DIR"
docker compose up -d --build --remove-orphans
docker image prune -f >/dev/null 2>&1 || true

# --- 7. Автообновление: раз в час сервер сам проверяет GitHub и ставит новую версию
cat > /usr/local/bin/cpsync-update <<UPD
#!/usr/bin/env bash
NEW=\$(curl -fsS --max-time 15 -H 'Accept: application/vnd.github.sha' "https://api.github.com/repos/$REPO/commits/$BRANCH" || true)
OLD=\$(cat $DIR/.commit 2>/dev/null || true)
[ -n "\$NEW" ] && [ "\$NEW" != "\$OLD" ] || exit 0
curl -fsSL "https://raw.githubusercontent.com/$REPO/$BRANCH/deploy/install.sh" | CPSYNC_REPO=$REPO CPSYNC_BRANCH=$BRANCH CPSYNC_QUICK=1 bash
UPD
chmod +x /usr/local/bin/cpsync-update
cat > /etc/systemd/system/cpsync-update.service <<UNIT
[Unit]
Description=CP Sync auto-update
[Service]
Type=oneshot
ExecStart=/usr/local/bin/cpsync-update
UNIT
cat > /etc/systemd/system/cpsync-update.timer <<UNIT
[Unit]
Description=CP Sync auto-update (hourly)
[Timer]
OnBootSec=10min
OnUnitActiveSec=1h
[Install]
WantedBy=timers.target
UNIT
systemctl daemon-reload >/dev/null 2>&1 && systemctl enable --now cpsync-update.timer >/dev/null 2>&1 || true
[ -n "${CPSYNC_QUICK:-}" ] && { echo "CP Sync обновлён"; exit 0; }

say "Жду HTTPS-сертификат для $DOMAIN…"
for _ in $(seq 1 60); do
  if curl -fsS --max-time 5 "https://$DOMAIN/healthz" >/dev/null 2>&1; then OK=1; break; fi
  sleep 3
done

echo
if [ "${OK:-}" = 1 ]; then
  printf '\033[1;32mГотово! CP Sync работает:  https://%s\033[0m\n' "$DOMAIN"
else
  printf '\033[1;33mCP Sync запущен, но HTTPS ещё не готов. Через пару минут откройте https://%s\033[0m\n' "$DOMAIN"
  echo "Проверьте, что порты 80 и 443 открыты у хостинга. Журнал: cd $DIR && docker compose logs caddy"
fi
echo "Первый зарегистрированный пользователь станет администратором."
echo "Обновление — та же команда установки. Данные лежат в $DATA."
