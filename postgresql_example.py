# python psycopg2 library example

# import psycopg2
import psycopg2
import os

conn = None
cur = None

try:
    #  Connect to a PostgreSQL database
    conn = psycopg2.connect(
        dbname=os.environ.get('PG_DB', 'database'),
        user=os.environ.get('PG_USER', 'username'),
        password=os.environ.get('PG_PASSWORD', 'password'),
        host=os.environ.get('PG_HOST', 'localhost'),
        port=os.environ.get('PG_PORT', '5432')
    )

    # Create cursor object to execute database commands and queries
    cur = conn.cursor()

    # Create a table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id serial PRIMARY KEY,
            name varchar(50),
            email varchar(50)
        )
    """)

    # Insert data into a table
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s) ",
                ("Jaspal", "jaspal@mail.com"))

    # Commit changes to the database
    conn.commit()

    # Query the database for all users
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

    # Print the results
    print(rows)

finally:
    # Close communication with the database
    if cur:
        cur.close()
    if conn:
        conn.close()
