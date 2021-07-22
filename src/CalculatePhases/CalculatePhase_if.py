from abc import abstractmethod
from abc import ABCMeta
import os
import sys
sys.path.append(os.path.abspath(".."))

try:
    from src.Manager_if import Manager_if as Manager
except ModuleNotFoundError:
    from .src.Manager_if import Manager_if as Manager

class CalculatePhase_if(metaclass=ABCMeta):
    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        raise PermissionError

    @classmethod
    def get_instance(cls):
        return cls._instance if cls._instance else cls.__new__(cls)

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
