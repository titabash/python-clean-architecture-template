import dataset
import os
from infrastructure.interface.idatabase import IDatabase
from utilities.logger.logging import log, get_logger

logger = get_logger()


class SQL(IDatabase):

    @log(logger)
    def __init__(self, dbName, tblName, user=None, pwd=None, dbType='postgresql', port=5432):
        user = user if user is not None else os.environ["SQL_USER"]
        pwd = pwd if pwd is not None else os.environ["SQL_PASS"]
        self.db = dataset.connect(
            f"{dbType}://{user}:{pwd}@{os.environ['SQL_ENDPOINT']}:{port}/{dbName}")
        self.db.begin()
        self.table = self.db[tblName]  # DB名を設定

    @log(logger)
    def find_one(self, filters={}):
        return self.table.find_one(**filters)

    @log(logger)
    def find(self, filters={}):
        return self.table.find(**filters)

    @log(logger)
    def insert(self, record):
        try:
            result = self.table.insert(record)
            self.db.commit()
            return result
        except Exception as e:
            self.db.rollback()
            # logger.error(e)
            raise e

    @log(logger)
    def update(self, record, filter):
        try:
            result = self.table.update(record, **filter)
            self.db.commit()
            return result
        except Exception as e:
            self.db.rollback()
            # logger.error(e)
            raise e

    @log(logger)
    def delete(self, filter=None):
        try:
            result = self.table.delete(**filter)
            self.db.commit()
            return result
        except Exception as e:
            self.db.rollback()
            # logger.error(e)
            raise e


if __name__ == '__main__':
    sql = SQL(dbName='pgtest', tblName='testtbl')

    print('--------------------Register--------------------')
    result = sql.insert({'name': 'Mike', 'salary': 400000})
    print(type(result))
    print(result)

    print('--------------------Check--------------------')
    result = sql.find({'name': 'Mike'})
    for record in result:
        print(record)

    print('--------------------Delete--------------------')
    result = sql.delete({'name': 'Mike'})
    print(type(result))
    print(result)

    print('--------------------Check--------------------')
    find = sql.find()
    for doc in find:
        print(doc)
