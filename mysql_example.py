# python mysql library example

# import pymysql module
import pymysql
import os

conn = None
cur = None

try:

    # Connect to the database
    conn = pymysql.connect(
        host=os.environ.get('MYSQL_HOST', 'localhost'),
        port=int(os.environ.get('MYSQL_PORT', '3306')),
        user=os.environ.get('MYSQL_USER', 'root'),
        password=os.environ.get('MYSQL_PASSWORD', 'password'),
        database=os.environ.get('MYSQL_DB', 'database')
    )

    # Create a cursor object
    cur = conn.cursor()

    # Create a table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT NOT NULL AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            PRIMARY KEY (id)
        )
    ''')

    # Commit the transaction
    conn.commit()

    # Execute the query to insert data
    cur.execute('''
            INSERT INTO users (name, email) VALUES (%s, %s), (%s, %s)
            ''', ('Singh', 'singh@mail.com', 'Jaspal', 'jaspal@mail.com'))

    # Commit the transaction
    conn.commit()

    # Execute the query to select data
    cur.execute('SELECT * FROM users')

    # Fetch the results
    rows = cur.fetchall()

    # Print the results
    print(rows)

finally:
    # Close the cursor and connection when finished
    if cur:
        cur.close()
    if conn:
        conn.close()
