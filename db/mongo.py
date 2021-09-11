from pymongo import MongoClient
import os


class Mongo(object):

    def __init__(self, dbName, collectionName, user='root', pwd='pass', port=27017):
        if os.environ['ENV'] == 'local':
            self.client = MongoClient('mongo_db', port)
        elif os.environ['ENV'] == 'stg':
            self.client = MongoClient('staging.com', port)
        elif os.environ['ENV'] == 'prod':
            self.client = MongoClient('production.com', port)
        else:  # dev
            self.client = MongoClient('development.com', port)

        self.client[dbName].authenticate(user, pwd)
        self.db = self.client[dbName]  # DB名を設定
        self.collection = self.db.get_collection(collectionName)

    def find_one(self, projection=None, filter=None, sort=None):
        return self.collection.find_one(projection=projection, filter=filter, sort=sort)

    def find(self, projection=None, filter=None, sort=None):
        return self.collection.find(projection=projection, filter=filter, sort=sort)

    def insert_one(self, document):
        return self.collection.insert_one(document)

    def insert_many(self, documents):
        return self.collection.insert_many(documents)

    def update_one(self, filter, update):
        return self.collection.update_one(filter, update)

    def update_many(self, filter, update):
        return self.collection.update_many(filter, update)

    def replace_one(self, filter, replacement):
        return self.collection.replace_one(filter, replacement)

    def find_one_and_replace(self, filter, replacement):
        return self.collection.find_one_and_replace(filter, replacement)

    def delete_one(self, filter):
        return self.collection.delete_one(filter)

    def delete_many(self, filter):
        return self.collection.delete_many(filter)

    def find_one_and_delete(self, filter):
        return self.collection.find_one_delete(filter)


if __name__ == '__main__':
    mongo = Mongo(dbName='test', collectionName='testCollections',
                  user='testUser', pwd='password')

    print('--------------------Register--------------------')
    result = mongo.insert_one({'name': 'Mike', 'salary': 400000})
    print(type(result))
    print(result)
    print(result.inserted_id)

    print('--------------------Check--------------------')
    find = mongo.find()
    for doc in find:
        print(doc)

    print('--------------------Delete--------------------')
    result = mongo.delete_one({'name': '加藤'})
    print(type(result))
    print(result)

    print('--------------------Check--------------------')
    find = mongo.find()
    for doc in find:
        print(doc)
