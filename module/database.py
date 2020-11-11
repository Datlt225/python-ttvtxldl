import pymongo


def connectToDatabase(collection):
    myClient = pymongo.MongoClient('mongodb://localhost:27017/')
    myDataBase = myClient['laodong']
    myCollection = myDataBase[collection]
    return myCollection


def insertToDataBase(key, value, database):
    database.update_one(key, value, upsert=True)
