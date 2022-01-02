from abc import ABCMeta, abstractmethod


class IHello(metaclass=ABCMeta):
    @abstractmethod
    def hello(self, event) -> str:
        raise NotImplementedError()
