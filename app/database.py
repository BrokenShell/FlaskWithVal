import os

from dotenv import load_dotenv
from pymongo import MongoClient


class Database:
    load_dotenv()
    collection = MongoClient(
        os.getenv("MONGO_URL"),
    )["Database"]["Collection"]

    def find(self, query: dict):
        return self.collection.find(query, {"_id": False})

    def insert(self, record: dict):
        self.collection.insert_one(record)

    def delete(self, query: dict):
        self.collection.delete_one(query)

    def update(self, query: dict, update: dict):
        self.collection.update_one(query, {"$set": update})
