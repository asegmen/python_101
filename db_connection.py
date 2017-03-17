from pymongo import MongoClient

conn = MongoClient("localhost:27017")


class DbConnection:
    def __init__(self):
        self.db = conn.test

    def get_all_data(self):
        cursor = self.db.restaurants.find({})
        return cursor

    def get_by_id(self, _id):
        return self.db.restaurants.find_one({"restaurant_id": _id})
