import sqlite3
import os

def test_sqlite():
    db_file = 'test_integration.db'
    
    try:
        if os.path.exists(db_file):
            os.remove(db_file)
        
        conn = sqlite3.connect(db_file)
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
        
        conn.close()
        print("✓ SQLite test passed")
        
    finally:
        if os.path.exists(db_file):
            os.remove(db_file)

if __name__ == '__main__':
    test_sqlite()
