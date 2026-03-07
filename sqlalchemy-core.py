# python sqlalchemy library example

import sqlalchemy as db
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

# Create an engine to connect to the database
engine = create_engine('dialect[+driver]://user:password@host/dbname')
# Define metadata for the database schema
metadata_obj = db.MetaData()

# Define a table to store information about users
users = Table(
	'users',
	metadata_obj,
	Column('id', Integer, primary_key=True),
	Column('name', String),
	Column('email', String),
)

# Create the table in the database
metadata_obj.create_all(engine)

# Insert some data into the table
connection = engine.connect()

try:

	# insert some data into the table
	with connection.begin():
		connection.execute(users.insert(), [
			{'name': 'Jaspal', 'email': 'jaspal@mail.com'},
			{'name': 'Singh', 'email': 'singh@mail.com'},
		])

	# Query the database to retrieve the inserted data
	result = connection.execute(users.select())
	rows = result.fetchall()

	for row in rows:
		print(row)
		# Output: (1, 'Jaspal', 'jaspal@mail.com')
		# Output: (2, 'Singh', 'singh@mail.com')

finally:
	# Close the connection to the database
	connection.close()
