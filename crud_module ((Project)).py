from pymongo import MongoClient
from pymongo.errors import PyMongoError

class CRUD:
    def __init__(self):
        try:
            self.client = MongoClient(
                "mongodb://aacuser:SNHU1234@nv-desktop-services.apporto.com:30634/?authSource=admin"
            )
            self.database = self.client["AAC"]
            self.collection = self.database["animals"]
        except PyMongoError as e:
            print(f"Connection Error: {e}")
            raise


    def create(self, data):
        """
        Inserts a document into the collection.
        Returns True if insertion is acknowledged, else False.
        """
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
        """
        Queries documents from the collection.
        Returns the results as a list.
        """
        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except PyMongoError as e:
            print(f"Read Error: {e}")
            return []

    def update(self, query, new_values):
        """
        Updates documents in the collection that match the query.
        Returns the number of documents modified.
        """
        try:
            result = self.collection.update_many(query, {'$set': new_values})
            return result.modified_count
        except PyMongoError as e:
            print(f"Update Error: {e}")
            return 0

    def delete(self, query):
        """
        Deletes documents from the collection that match the query.
        Returns the number of documents deleted.
        """
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError as e:
            print(f"Delete Error: {e}")
            return 0

