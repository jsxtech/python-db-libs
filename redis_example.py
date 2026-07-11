# python redis library example

# Import the Redis library
import redis
import os

r = None

try:

    # Create a Redis client object
    r = redis.Redis(
        host=os.environ.get('REDIS_HOST', 'localhost'),
        port=int(os.environ.get('REDIS_PORT', '6379')),
        db=int(os.environ.get('REDIS_DB', '0'))
    )

    # Set a key-value pair
    r.set('name', 'Jaspal')
    r.set('email', 'jaspal@mail.com')

    # Retrieve the value of the key
    value = r.get('name')
    print(value)  # Output: b'Jaspal'

    # Add an item to a set
    r.sadd('users_set', 'Jaspal')
    r.sadd('users_set', 'jaspal@mail.com')

    # Retrieve the members of the set
    users_set = r.smembers('users_set')
    print(users_set)  # Output: {b'Jaspal', b'jaspal@mail.com'}

    # Create a list
    r.lpush('users_list', 'Jaspal')
    r.lpush('users_list', 'jaspal@mail.com')

    # Retrieve the list
    users_list = r.lrange('users_list', 0, -1)
    print(users_list)  # Output: [b'jaspal@mail.com', b'Jaspal']

    # Create a hash
    r.hset('users_hash', 'name', 'Jaspal')
    r.hset('users_hash', 'email', 'jaspal@mail.com')

    # Retrieve the hash
    users_hash = r.hgetall('users_hash')
    print(users_hash)  # Output: {b'name': b'Jaspal', b'email': b'jaspal@mail.com'}

finally:
    # Close the Redis client
    if r:
        r.close()
