# Оценки ManageBac

Все задания и оценки из ManageBac на одной странице, без захода в каждое задание.

* **Все задания** — таблица: дата, предмет, задание, оценка (критерии A–D или баллы), комментарий учителя. Клик по строке раскрывает комментарий целиком, название ведёт в ManageBac.
* **По предметам** — для каждого предмета матрица критериев A/B/C/D по всем работам и средние.
* Карточки предметов сверху: средние по критериям (по summative-работам, если они есть) и средний процент по баллам.
* Фильтры: предмет, Summative/Formative, триместр, «только с оценкой», поиск.
* Новые оценки отмечаются красной точкой.
* Работает на телефоне (можно добавить на экран «Домой»).

## Как это работает

Вход на сайт — той же почтой и паролем, что и в ManageBac. Сервер проверяет их в ManageBac и запоминает
(файл `/var/lib/grades/users.json`, доступен только root), чтобы сам заходить и обновлять оценки:
при открытии сайта, если данным больше 20 минут, кнопкой «Обновить» и в фоне раз в 2 часа.
Каждый видит только свои оценки.

Данные берутся со страниц `Classes → Tasks` всех классов (одна страница на класс и триместр).

## Установка на сервер

```bash
curl -fsSL https://raw.githubusercontent.com/Nmk102/cpsync/main/deploy/install.sh | sudo bash
```

Скрипт ставит Docker, удаляет CP Sync (если был; его данные архивируются в `/root/cpsync-backup-*.tar.gz`),
запускает сайт с HTTPS и включает автообновление из GitHub (проверка раз в 10 минут). Адрес: `https://<IP-через-дефисы>.sslip.io`.

| Что | Как |
|---|---|
| Журнал | `cd /opt/grades && docker compose logs -f app` |
| Перезапуск | `cd /opt/grades && docker compose restart` |
| Свой адрес | `curl … \| sudo GRADES_DOMAINS=grades.example.com bash` |
| Забыть все пароли и сессии | `rm /var/lib/grades/users.json /var/lib/grades/sessions.json` |

## Разработка

```bash
pip install requests beautifulsoup4
cd app && DATA_DIR=/tmp/grades python server.py   # http://localhost:8080
python tests/test_parse.py
```

CP Sync (прежнее содержимое репозитория) лежит в ветке `cpsync-archive`.
