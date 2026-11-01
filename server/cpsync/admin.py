"""Администрирование CP Sync из командной строки сервера.

    docker compose exec app python -m cpsync.admin users
    docker compose exec app python -m cpsync.admin reset-password <логин>
    docker compose exec app python -m cpsync.admin delete-user <логин>
"""
import os
import secrets
import sys

from .storage import Storage


def main():
    st = Storage(os.environ.get('CPSYNC_DATA', 'cpsync-data'))
    args = sys.argv[1:]
    if args[:1] == ['users']:
        for r in st.q('SELECT u.login, u.is_admin, (SELECT COUNT(*) FROM projects p WHERE p.user_id = u.id) AS n '
                      'FROM users u ORDER BY u.id'):
            print('%-32s проектов: %-4d %s' % (r['login'], r['n'], 'админ' if r['is_admin'] else ''))
    elif args[:1] == ['reset-password'] and len(args) == 2:
        r = st.q1('SELECT id FROM users WHERE login = ?', (args[1],))
        if not r:
            sys.exit('нет такого пользователя')
        pw = secrets.token_urlsafe(9)
        st.set_password(r['id'], pw)
        st.db.execute('DELETE FROM tokens WHERE user_id = ?', (r['id'],))
        print('Новый пароль для %s: %s  (все устройства отключены)' % (args[1], pw))
    elif args[:1] == ['delete-user'] and len(args) == 2:
        st.db.execute('PRAGMA foreign_keys = ON')
        n = st.db.execute('DELETE FROM users WHERE login = ?', (args[1],)).rowcount
        print('удалено' if n else 'нет такого пользователя')
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
