# https://docs.mongodb.org/getting-started/python/query/


from pymongo import MongoClient

client = MongoClient()
# Make a new database
db = client['pymongo']


# From dictionary (fruit)
data = {"apple" : "green", "banna" : "yellow", "orange" : "orange"}
db.fruit.insert(data)


# From dict of dicts (veg)
data = {
  "list" : {
    "date" : "5/23/82",
    "employee" : "dylan"
  },
  "veg" : {
    "onion" : {
      "color" : "white",
      "price" : ".99",
      "age" : 7
    },
    "squash" : {
      "color" : "yellow",
      "price" : "2.49",
      "age" : 3
    },
    "pickle" : {
      "color" : "green",
      "price" : "1.99",
      "age" : 4
    }
  },
  "profits" : [
    13,
    12,
    8,
    5,
    3,
    1
  ]
}





db.veg.insert(data)





