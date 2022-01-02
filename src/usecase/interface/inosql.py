from abc import ABCMeta, abstractmethod


class INoSQL(metaclass=ABCMeta):
    @abstractmethod
    def find(self, event) -> str:
        raise NotImplementedError()
