# python cassandra library example

# Import the Cassandra driver
from cassandra.cluster import Cluster
import os

cluster = None
session = None

try:

    # Create a session instance
    cassandra_host = os.environ.get('CASSANDRA_HOST', '127.0.0.1')
    cassandra_port = int(os.environ.get('CASSANDRA_PORT', '9042'))
    cluster = Cluster([cassandra_host], port=cassandra_port)
    session = cluster.connect()

    # Create a keyspace
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS mykeyspace
        WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '3'}
    """)

    # Create a table
    session.execute("""
        CREATE TABLE IF NOT EXISTS mykeyspace.users
        (id int PRIMARY KEY, name text, email text)
    """)

    # Insert a row using prepared statement
    prepared = session.prepare("INSERT INTO mykeyspace.users (id, name, email) VALUES (?, ?, ?)")
    session.execute(prepared, (1, 'Jaspal', 'jaspal@mail.com'))

    # Query the table
    rows = session.execute("SELECT * FROM mykeyspace.users")
    for row in rows:
        print(row.id, row.name, row.email)

finally:
    # Close the session and cluster
    if session:
        session.shutdown()
    if cluster:
        cluster.shutdown()
