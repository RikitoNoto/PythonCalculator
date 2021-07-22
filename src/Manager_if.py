from abc import ABCMeta
from abc import abstractmethod

try:
    from Calculator import Calculator
except ModuleNotFoundError:
    from .Calculator import Calculator

class Manager_if(metaclass=ABCMeta):

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

    @abstractmethod
    def append_current_value(self):
        pass

    @abstractmethod
    def get_current_phase(self):
        pass


    calculator = property(doc="Calculatorインスタンス")
    gui = property(doc="GUIManagerインスタンス")
    history = property(doc="過去の計算結果のログ")
    current_phase = property(fget=get_current_phase, doc="現在のフェーズクラスインスタンス")