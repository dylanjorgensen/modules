# http://docs.mongodb.org/manual/reference/operator/query/


# Operators use the same syntax as field names but with a $ in front

from pymongo import MongoClient
import pprint


client = MongoClient()
db = client.pymongo

# --- Inequality Operators --- #

# # Range operators
# $gt: greater than
# $lt: less than
# $gte: greater than or equial to
# $lte: less than or equal to
# $ne: Not equal to

#q = {"age" : {"$lt" : 6}}
query = db.veg.find({"profits": {"$ne" : 5 }})

import pprint
for i in query:
    pprint.pprint(i)
print "count:", query.count()
