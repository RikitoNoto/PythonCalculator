from abc import abstractmethod
from abc import ABCMeta

class CalculatePhase_if(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def get_instance(cls):
        pass

    @abstractmethod
    def push_number(self, input):
        pass

    @abstractmethod
    def push_operator(self, input):
        pass

    @abstractmethod
    def push_equal(self, input):
        pass

    @abstractmethod
    def push_ac(self, input):
        pass
