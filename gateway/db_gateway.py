from utilities.logger.logging import log, get_logger
from usecase.interface.inosql import INoSQL
from infrastructure.db.mongo import Mongo

logger = get_logger()


class DbController(INoSQL):
    @log(logger)
    def __init__(self, db_name="test", collection_name="testCollection"):
        self.mongo = Mongo(dbName=db_name, collectionName=collection_name)

    @log(logger)
    def find(self):
        data = self.mongo.find()
        return data
