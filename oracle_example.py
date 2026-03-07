# python cx_Oracle library example

# Import the cx_Oracle module
import cx_Oracle

conn = None
cur = None

try:

    # Connect to Oracle database
    conn = cx_Oracle.connect('username/password@hostname:port_number/db_name')

    # Create a cursor object
    cur = conn.cursor()

    try:

        # Create a table
        cur.execute('''CREATE TABLE
                        Users(id number(10), name varchar2(20), email varchar2(30))''')

    except cx_Oracle.DatabaseError:
        pass # Table already exists

    # Insert a new row into the user's table
    cur.execute("INSERT INTO users (name, email) VALUES (:1, :2)", ('Jaspal', 'jaspal@mail.com'))

    # commit changes to db
    conn.commit()

    # Execute a SQL query
    cur.execute('SELECT * FROM users')

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
