from abc import abstractmethod
from abc import ABCMeta
import os
import sys

sys.path.append(os.path.abspath(".."))

try:
    from src.Manager_if import Manager_if as Manager
except ModuleNotFoundError:
    from .src.Manager_if import Manager_if as Manager


class CalculatePhaseTemplate_ab(metaclass=ABCMeta):
    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        cls._instance = super().__new__(cls)
        cls._instance._initialize()
        return cls._instance

    def __init__(self):
        raise PermissionError

    def _initialize(self):
        pass

    @classmethod
    def get_instance(cls):
        return cls._instance if cls._instance else cls.__new__(cls)
