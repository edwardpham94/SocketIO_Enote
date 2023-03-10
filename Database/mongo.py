import pymongo
from pymongo import MongoClient

cluster = pymongo.MongoClient(
    "mongodb+srv://computernetwork:computernetwork_21clc07@cluster0.jq2th.mongodb.net/?retryWrites=true&w=majority")

db = cluster["e-note"]
collection = db["users"]

data = collection.find()

for element in data:
    print(element["username"], element["password"])
