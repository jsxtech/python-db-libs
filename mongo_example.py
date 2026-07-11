# python mongo library example

# Import the PyMongo library
import pymongo
import os

client = None

try:

    # Create a client, database, and collection instances
    mongo_host = os.environ.get('MONGO_HOST', 'localhost')
    mongo_port = os.environ.get('MONGO_PORT', '27017')
    client = pymongo.MongoClient(f'mongodb://{mongo_host}:{mongo_port}/')
    db = client['my_database']
    collection = db['my_collection']

    # Insert a document
    document = {'name': 'Jaspal', 'email': 'jaspal@mail.com'}
    result = collection.insert_one(document)

    # Find all documents
    find_all_result = collection.find()
    for doc in find_all_result:
        print(doc)

    # Find a document
    query = {'name': 'Jaspal'}
    find_one_result = collection.find_one(query)
    print(find_one_result)

    # Update a document
    query = {'name': 'Jaspal'}
    new_values = {'$set': {'email': 'jaspal_new@mail.com'}}
    update_result = collection.update_one(query, new_values)
    print(update_result)

    # Delete a document
    query = {'name': 'Jaspal'}
    delete_result = collection.delete_one(query)
    print(delete_result)

finally:
    # Close the connection
    if client:
        client.close()
