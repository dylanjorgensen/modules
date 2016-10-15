# http://docs.mongodb.org/manual/core/read-operations-introduction/


from pymongo import MongoClient

client = MongoClient()
db = client.pymongo


# Returns all the documents with all the fields
query = db.veg.find()

# Returns all from parent node of specific value
query = db.veg.find({"report" : "today"})


# Add projection selection (shape of results)
query = db.veg.find({}, {"list" : 1})


query = db.veg.find({'profits' : {"$gte" : 3}})


# Monogs power is in that you can query data structures
# not just scalers like stings and ints

# Will find 8 inside array and return document class
query = db.veg.find({"profits" : 8})

# Will find all douments with any digit in the array
# ("$all") is the opposit
query = db.veg.find({"profits" : {"$in" : [3, 4, 7, 9]}})



import pprint
for i in query[0:1]:
    pprint.pprint(i)
print "count:", query.count()
