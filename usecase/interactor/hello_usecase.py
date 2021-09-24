import sys
import os

from utilities.logger.logging import log, get_logger
from usecase.interface.ihello import IHello
from entity.hello_entity import HelloEntity
from gateway.db_gateway import DbController

logger = get_logger()


class Hello(IHello):
    # @log(logger)
    # def __init__(self, d: dict):
    #     self._d = d

    @log(logger)
    def hello(self, event='test') -> str:
        hello = HelloEntity(
            environment=os.environ["ENV"], py_version=sys.version, event=event)
        text = f'Hello Batch from {hello.environment} using Python {hello.py_version}!\nEvent Object is {hello.event}'
        return text

    @log(logger)
    def find_all(self) -> str:
        db_controller = DbController()
        data = db_controller.find()
        return data
