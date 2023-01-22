from pymongo import MongoClient

class Database:
    def __init__(self, connectionString):
        self.client = MongoClient(connectionString)
        self.db = self.client.Authentication

    def insert_data(self, collectionName, data):
        self.db[collectionName].insert_one(data)

    def find_data(self, collectionName, query):
        rawResult = self.db[collectionName].find(query)
        resultArr = []

        for result in rawResult:
            resultArr.append(str(result["_id"]))

        return resultArr