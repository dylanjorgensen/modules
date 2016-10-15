# https://docs.mongodb.org/getting-started/python/client/


from pymongo import MongoClient

# defaults to the MongoDB main client instance
client = MongoClient()
# print client.database_names() # Returns list of database names
# print client.address  # Returns host address and port number

db = client['pymongo']  # Selects a database for use or create new

# Targeting a collection
query = db.autos.find({"assembly" : "Finland"})

# Deleting a collection
# db.collection.drop()


import pprint
for i in query:
    pprint.pprint(i)