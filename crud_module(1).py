from pymongo import MongoClient
from pymongo.errors import PyMongoError

class CRUD:
    def __init__(self, username, password):
        try:
            HOST = "nv-desktop-services.apporto.com"
            PORT = 30634
            DB = "AAC"
            COL = "animals"
            uri = f"mongodb://{username}:{password}@{HOST}:{PORT}/?authSource=admin"
            self.client = MongoClient(uri)
            self.database = self.client[DB]
            self.collection = self.database[COL]
        except PyMongoError as e:
            print(f"Connection Error: {e}")
            raise

    def create(self, data):
        if data:
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            except PyMongoError as e:
                print(f"Create Error: {e}")
                return False
        else:
            raise ValueError("Nothing to insert: data is empty.")

    def read(self, query):
        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except PyMongoError as e:
            print(f"Read Error: {e}")
            return []

    def update(self, query, new_values):
        try:
            result = self.collection.update_many(query, {'$set': new_values})
            return result.modified_count
        except PyMongoError as e:
            print(f"Update Error: {e}")
            return 0

    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError as e:
            print(f"Delete Error: {e}")
            return 0
