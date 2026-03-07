# python cassandra library example

# Import the Cassandra driver
from cassandra.cluster import Cluster

cluster = None
session = None

try:

    # Create a session instance
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()

    # Create a keyspace
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS mykeyspace
        WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '3'}
    """)

    # Create a table
    session.execute("""
        CREATE TABLE IF NOT EXISTS mykeyspace.mytable
        (id int PRIMARY KEY, name text, age int)
    """)

    # Insert a row using prepared statement
    prepared = session.prepare("INSERT INTO mykeyspace.mytable (id, name, age) VALUES (?, ?, ?)")
    session.execute(prepared, (1, 'Jaspal', 30))

    # Query the table
    rows = session.execute("SELECT * FROM mykeyspace.mytable")
    for row in rows:
        print(row.id, row.name, row.age)

finally:
    # Close the session and cluster
    if session:
        session.shutdown()
    if cluster:
        cluster.shutdown()
