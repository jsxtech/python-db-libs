# python sqlalchemy orm example

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Create a database engine
engine =  create_engine('dialect[+driver]://user:password@host/dbname')

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Define a model
class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	email = Column(String)

	def __repr__(self):
            return f"<User(name='{self.name}', email='{self.email}')>"

# Create a table in the database
Base.metadata.create_all(engine)

# Create a new user
new_user = User(name='Jaspal', email='jaspal@mail.com')

# Add the user to the database
session = Session()

try:

	session.add(new_user)
	session.commit()

	# Query the database for all users
	users = session.query(User).all()

	# Print the results
	for user in users:
		print(user)

finally:
	# Close the session
	session.close()
