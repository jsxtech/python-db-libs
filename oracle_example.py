# python cx_Oracle library example

# Import the cx_Oracle module
import cx_Oracle
import os

conn = None
cur = None

try:

    # Connect to Oracle database
    dsn = cx_Oracle.makedsn(
        os.environ.get('ORACLE_HOST', 'localhost'),
        os.environ.get('ORACLE_PORT', '1521'),
        service_name=os.environ.get('ORACLE_DB', 'XEPDB1')
    )
    conn = cx_Oracle.connect(
        user=os.environ.get('ORACLE_USER', 'username'),
        password=os.environ.get('ORACLE_PASSWORD', 'password'),
        dsn=dsn
    )

    # Create a cursor object
    cur = conn.cursor()

    try:

        # Create a table with GENERATED ALWAYS AS IDENTITY for auto-increment id
        cur.execute('''CREATE TABLE Users(
                        id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                        name VARCHAR2(20),
                        email VARCHAR2(30))''')

    except cx_Oracle.DatabaseError:
        pass  # Table already exists

    # Insert a new row into the user's table
    cur.execute("INSERT INTO Users (name, email) VALUES (:1, :2)",
                ('Jaspal', 'jaspal@mail.com'))

    # commit changes to db
    conn.commit()

    # Execute a SQL query
    cur.execute('SELECT * FROM Users')

    # Fetch all rows
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

finally:
    # Close the cursor and connection
    if cur:
        cur.close()
    if conn:
        conn.close()
