from pymongo import MongoClient


client = MongoClient()
db = client['pymongo']  # Selects a database for use or create new


#query = db.veg.find({"report" : "today"})
query = db.veg.find({}, {"list" : 1})

for i in query:
    print i
print "count", query.count()