import sqlite3
import os
import tempfile


def test_sqlite():
    # Use a temp directory so the test never writes into the working directory.
    with tempfile.TemporaryDirectory() as tmpdir:
        db_file = os.path.join(tmpdir, 'test_integration.db')

        conn = sqlite3.connect(db_file)
        try:
            cur = conn.cursor()

            cur.execute('''CREATE TABLE IF NOT EXISTS users
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)''')

            cur.execute("INSERT INTO users (name, email) VALUES (?, ?)",
                        ('TestUser', 'test@mail.com'))
            conn.commit()

            cur.execute('SELECT * from users')
            result = cur.fetchall()

            assert len(result) == 1
            assert result[0][1] == 'TestUser'
            assert result[0][2] == 'test@mail.com'
        finally:
            conn.close()

        print("\u2713 SQLite test passed")


if __name__ == '__main__':
    test_sqlite()
