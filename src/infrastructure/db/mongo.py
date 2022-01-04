from pymongo import MongoClient
import os


class Mongo():

    def __init__(self, dbName, collectionName, user=None, pwd=None, port=27017):
        self.client = MongoClient(os.environ['MONGO_ENDPOINT'], port)
        user = user if user is not None else os.environ["MONGO_USER"]
        pwd = pwd if pwd is not None else os.environ["MONGO_PASS"]
        self.client[dbName].authenticate(user, pwd)
        self.db = self.client[dbName]  # DB名を設定
        self.collection = self.db.get_collection(collectionName)

    def find_one(self, projection=None, filter=None, sort=None):
        return self.collection.find_one(projection=projection, filter=filter, sort=sort)

    def find(self, projection=None, filter=None, sort=None):
        return self.collection.find(projection=projection, filter=filter, sort=sort)

    def insert(self, document):
        return self.collection.insert_one(document)

    def insert_many(self, documents):
        return self.collection.insert_many(documents)

    def update(self, filter, document):
        return self.collection.update_one(filter, document)

    def update_many(self, filter, documents):
        return self.collection.update_many(filter, documents)

    def replace_one(self, filter, document):
        return self.collection.replace_one(filter, document)

    def find_one_and_replace(self, filter, documents):
        return self.collection.find_one_and_replace(filter, documents)

    def delete(self, filter):
        return self.collection.delete_one(filter)

    def delete_many(self, filter):
        return self.collection.delete_many(filter)

    def find_one_and_delete(self, filter):
        return self.collection.find_one_delete(filter)


if __name__ == '__main__':
    mongo = Mongo(dbName='test', collectionName='testCollections')

    print('--------------------Register--------------------')
    result = mongo.insert({'name': 'Mike', 'salary': 400000})
    print(type(result))
    print(result)
    print(result.inserted_id)

    print('--------------------Check--------------------')
    find = mongo.find()
    for doc in find:
        print(doc)

    print('--------------------Delete--------------------')
    result = mongo.delete({'name': 'Mike'})
    print(type(result))
    print(result)

    print('--------------------Check--------------------')
    find = mongo.find()
    for doc in find:
        print(doc)
