from abc import ABCMeta, abstractmethod


class IDatabase(metaclass=ABCMeta):
    # @abstractmethod
    def find_one(self):
        raise NotImplementedError()

    @abstractmethod
    def find(self):
        raise NotImplementedError()

    # @abstractmethod
    def insert(self):
        raise NotImplementedError()

    # @abstractmethod
    def update(self):
        raise NotImplementedError()

    # @abstractmethod
    def delete(self):
        raise NotImplementedError()
