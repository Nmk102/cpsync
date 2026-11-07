#!/usr/bin/env bash
# Оценки ManageBac — установка и обновление на VPS (Ubuntu 22.04/24.04, Debian 12).
#
#   curl -fsSL https://raw.githubusercontent.com/Nmk102/cpsync/main/deploy/install.sh | sudo bash
#
# Если на сервере стоит CP Sync, он будет остановлен и удалён
# (его данные сохраняются в архив /root/cpsync-backup-<дата>.tar.gz).
# Повторный запуск — обновление до последней версии (вход и оценки сохраняются).
set -euo pipefail

REPO="${GRADES_REPO:-${CPSYNC_REPO:-Nmk102/cpsync}}"
BRANCH="${GRADES_BRANCH:-${CPSYNC_BRANCH:-main}}"
DIR=/opt/grades
DATA=/var/lib/grades

say() { printf '\n\033[1;36m==> %s\033[0m\n' "$*"; }
die() { printf '\n\033[1;31mОшибка: %s\033[0m\n' "$*" >&2; exit 1; }

[ "$(id -u)" -eq 0 ] || die "запустите от root: добавьте sudo перед bash"

echo 'DPkg::Lock::Timeout "900";' > /etc/apt/apt.conf.d/99grades-lock
export DEBIAN_FRONTEND=noninteractive
retry() { local n=0; until "$@"; do n=$((n+1)); [ "$n" -ge 5 ] && return 1; echo "повтор через 20 с ($n/5)…"; sleep 20; done; }
command -v curl >/dev/null || retry bash -c 'apt-get update -qq && apt-get install -y -qq curl ca-certificates'

# --- 1. Docker
if ! command -v docker >/dev/null 2>&1; then
  say "Устанавливаю Docker…"
  retry bash -c 'curl -fsSL https://get.docker.com | sh >/dev/null' || die "не удалось установить Docker"
fi
systemctl enable --now docker >/dev/null 2>&1 || true
docker compose version >/dev/null 2>&1 || die "не найден docker compose"

# --- 2. Скачиваем код (до удаления CP Sync: если GitHub недоступен, ничего не ломаем)
say "Скачиваю сайт оценок ($REPO, ветка $BRANCH)…"
TMP=$(mktemp -d)
curl -fsSL "https://codeload.github.com/$REPO/tar.gz/refs/heads/$BRANCH" | tar xz -C "$TMP" --strip-components=1 \
  || die "не удалось скачать код с GitHub"
[ -f "$TMP/app/server.py" ] || die "в $REPO нет сайта оценок"

# --- 3. Удаляем CP Sync (если он есть)
OLD_DOMAIN=""
if [ -d /opt/cpsync ] || [ -f /etc/systemd/system/cpsync-update.timer ]; then
  say "Удаляю CP Sync…"
  OLD_DOMAIN=$(grep -s '^CPSYNC_DOMAIN=' /opt/cpsync/.env | cut -d= -f2- || true)
  systemctl disable --now cpsync-update.timer >/dev/null 2>&1 || true
  rm -f /etc/systemd/system/cpsync-update.timer /etc/systemd/system/cpsync-update.service /usr/local/bin/cpsync-update \
        /etc/apt/apt.conf.d/99cpsync-lock
  systemctl daemon-reload >/dev/null 2>&1 || true
  if [ -f /opt/cpsync/docker-compose.yml ]; then
    (cd /opt/cpsync && docker compose down -v --remove-orphans) || true
  fi
  docker ps -aq --filter "name=cpsync" | xargs -r docker rm -f >/dev/null 2>&1 || true
  docker image rm -f cpsync-app:latest cpsync-sandbox:latest >/dev/null 2>&1 || true
  if [ -d /var/lib/cpsync ] && [ -n "$(ls -A /var/lib/cpsync 2>/dev/null)" ]; then
    BK="/root/cpsync-backup-$(date +%Y%m%d-%H%M).tar.gz"
    tar czf "$BK" -C /var/lib cpsync && echo "данные CP Sync сохранены в $BK"
  fi
  rm -rf /opt/cpsync /var/lib/cpsync
fi
echo "$OLD_DOMAIN" | grep -q . && echo "$OLD_DOMAIN" > /root/.grades-old-domain || true
[ -z "$OLD_DOMAIN" ] && OLD_DOMAIN=$(cat /root/.grades-old-domain 2>/dev/null || true)

# --- 4. Ставим код
mkdir -p "$DIR" "$DATA"
chown 1000:1000 "$DATA" && chmod 700 "$DATA"
find "$DIR" -mindepth 1 -maxdepth 1 ! -name .env -exec rm -rf {} +
cp -a "$TMP/." "$DIR/"
rm -rf "$TMP"
curl -fsS --max-time 15 -H 'Accept: application/vnd.github.sha' \
  "https://api.github.com/repos/$REPO/commits/$BRANCH" > "$DIR/.commit" 2>/dev/null || true

# --- 5. Адреса сайта: <ip>.sslip.io (+ прежний адрес CP Sync, если был свой домен)
SAVED=$(grep -s '^GRADES_DOMAINS=' "$DIR/.env" | cut -d= -f2- || true)
DOMAINS="${GRADES_DOMAINS:-$SAVED}"
if [ -z "$DOMAINS" ]; then
  IP=$(curl -fsS4 --max-time 10 https://api.ipify.org || curl -fsS4 --max-time 10 https://ifconfig.me || true)
  [ -n "$IP" ] || die "не удалось узнать внешний IP — укажите адрес: GRADES_DOMAINS=..."
  DOMAINS="${IP//./-}.sslip.io"
  case "$OLD_DOMAIN" in ""|*sslip.io) ;; *) DOMAINS="$DOMAINS, $OLD_DOMAIN" ;; esac
fi
cat > "$DIR/.env" <<ENV
GRADES_DOMAINS=$DOMAINS
MB_SCHOOL=${MB_SCHOOL:-theislandprivateschool}
ENV

if command -v ufw >/dev/null 2>&1 && ufw status | grep -q 'Status: active'; then
  ufw allow 80/tcp >/dev/null; ufw allow 443/tcp >/dev/null; ufw allow 443/udp >/dev/null
fi

# --- 6. Запуск
say "Собираю и запускаю…"
cd "$DIR"
docker compose up -d --build --remove-orphans
docker image prune -f >/dev/null 2>&1 || true

# --- 7. Автообновление раз в час из GitHub
cat > /usr/local/bin/grades-update <<UPD
#!/usr/bin/env bash
NEW=\$(curl -fsS --max-time 15 -H 'Accept: application/vnd.github.sha' "https://api.github.com/repos/$REPO/commits/$BRANCH" || true)
OLD=\$(cat $DIR/.commit 2>/dev/null || true)
[ -n "\$NEW" ] && [ "\$NEW" != "\$OLD" ] || exit 0
curl -fsSL "https://raw.githubusercontent.com/$REPO/$BRANCH/deploy/install.sh" | GRADES_REPO=$REPO GRADES_BRANCH=$BRANCH GRADES_QUICK=1 bash
UPD
chmod +x /usr/local/bin/grades-update
cat > /etc/systemd/system/grades-update.service <<UNIT
[Unit]
Description=Grades site auto-update
[Service]
Type=oneshot
ExecStart=/usr/local/bin/grades-update
UNIT
cat > /etc/systemd/system/grades-update.timer <<UNIT
[Unit]
Description=Grades site auto-update (hourly)
[Timer]
OnBootSec=10min
OnUnitActiveSec=1h
[Install]
WantedBy=timers.target
UNIT
systemctl daemon-reload >/dev/null 2>&1 && systemctl enable --now grades-update.timer >/dev/null 2>&1 || true

FIRST="${DOMAINS%%,*}"
if [ -z "${GRADES_QUICK:-}${CPSYNC_QUICK:-}" ]; then
  say "Жду HTTPS-сертификат для $FIRST…"
  for _ in $(seq 1 60); do
    curl -fsS --max-time 5 "https://$FIRST/healthz" >/dev/null 2>&1 && { OK=1; break; }
    sleep 3
  done
fi
echo
printf '\033[1;32mГотово! Сайт с оценками:  https://%s\033[0m\n' "$FIRST"
echo "Войдите почтой и паролем от ManageBac. Журнал: cd $DIR && docker compose logs -f app"
