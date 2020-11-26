import pymongo


def connect_database(collection):
    my_client = pymongo.MongoClient('mongodb://localhost:27017/')
    my_database = my_client['laodong']
    return my_database[collection]


def insert_database(key, value, database):
    database.update_one(key, value, upsert=True)
