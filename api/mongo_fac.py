from pymongo import MongoClient
import os

class mongoFactory:
    def __init__(self):

        self.__mongoAddr = os.getenv('MONGO_ADDR')

        self.__client = MongoClient(self.__mongoAddr, 27017)

        self.__mongodb = self.__client.microservices

        self.__collection = self.__mongodb.tasks

    def insert(self, dictData):        
        mValid = self.__collection.insert_many(dictData).inserted_ids
        return mValid
    def update(self, filter, newSet):
        self.__collection.update(filter, {'$set':newSet})
    def delete(self, filter):
        self.__collection.delete_one(filter)
    def find(self, filter):
        mFindResult = self.__collection.find(filter)
        return mFindResult