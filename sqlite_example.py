# python sqlite library example

# Import the sqlite3 module
import sqlite3

conn = None

try:
    # Create a connection to the database
    conn = sqlite3.connect('test.db')

    # Create a cursor object
    cur = conn.cursor()

    # Create a table
    cur.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)''')

    # Insert some data
    cur.execute("INSERT INTO users (name, email) VALUES (?, ?)",
                ('Jaspal', 'jaspal@mail.com'))

    # Commit changes
    conn.commit()

    # Execute a SQL query
    cur.execute('SELECT * from users')
    result = cur.fetchall()

    # Print the result
    print(result)

finally:
    if conn:
        # Close the connection
        conn.close()

# Output:
# [(1, 'Jaspal', 'jaspal@mail.com')]
