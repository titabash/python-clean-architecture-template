from utilities.logger.logging import log, get_logger
from gateway.interface.idatabase import IDatabase
from infrastructure.db.mongo import Mongo

logger = get_logger()


class DbGateway(IDatabase):
    @log(logger)
    def __init__(self, db_name="test", collection_name="testCollection"):
        self.db = Mongo(dbName=db_name, collectionName=collection_name)

    @log(logger)
    def find(self):
        data = self.db.find()
        return data
