import sys
import os

from utilities.logger.logging import log, get_logger
from usecase.interface.ihello import IHello
from domain.hello_entity import HelloEntity
from domain.repository.db.db_repository import DbRepository

logger = get_logger()


class Hello(IHello):
    # @log(logger)
    # def __init__(self, d: dict):
    #     self._d = d

    @log(logger)
    def hello(self, event='test') -> str:
        hello = HelloEntity(
            environment=os.environ["MACHINE_ENV"], py_version=sys.version, event=event)
        text = f'Hello Batch from {hello.environment} using Python {hello.py_version}!\nEvent Object is {hello.event}'
        return text

    @log(logger)
    def find_all(self) -> str:
        db_repository = DbRepository()
        data = db_repository.find()
        return data
