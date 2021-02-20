from abc import ABC, abstractmethod

class Event(ABC):

    @property
    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def response(self):
        pass

if __name__ == '__main__':
    pass
