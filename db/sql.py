import dataset
import os


class SQL(object):

    def __init__(self, dbName, tblName, user='root', pwd='pass'):
        if os.environ["ENV"] == 'local':
            self.db = dataset.connect(
                f"postgresql://{user}:{pwd}@localhost:5432/{dbName}")
        elif os.environ["ENV"] == 'stg':
            self.db = dataset.connect(
                f"postgresql://{user}:{pwd}@staging:5432/{dbName}")
        elif os.environ["ENV"] == 'prod':
            self.db = dataset.connect(
                f"postgresql://{user}:{pwd}@production:5432/{dbName}")
        else:  # dev
            self.db = dataset.connect(
                f"postgresql://{user}:{pwd}@development:5432/{dbName}")

        self.table = self.db[tblName]  # DB名を設定

    def find_one(self, **kwargs):
        return self.table.find_one(kwargs)

    def find(self, **kwargs):
        return self.table.find(kwargs)

    def insert(self, document):
        return self.table.insert(document)

    def update(self, document, search):
        return self.table.insert(document, search)

    def delete(self, **kwargs):
        return self.table.delete(kwargs)
