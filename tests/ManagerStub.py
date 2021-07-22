import os
import sys
sys.path.append(os.path.abspath(".."))


try:
    from src.Manager_if import Manager_if
except ModuleNotFoundError:
    from .src.Manager_if import Manager_if

class ManagerStub(Manager_if):

    def push_number(self, input):
        pass

    def push_operator(self, input):
        pass

    def push_equal(self, input):
        pass

    def push_ac(self, input):
        pass

    def append_current_value(self):
        pass

    def get_current_phase(self):
        pass


    calculator = property(doc="Calculatorインスタンス")
    gui = property(doc="GUIManagerインスタンス")
    history = property(doc="過去の計算結果のログ")
    current_phase = property(fget=get_current_phase, doc="現在のフェーズクラスインスタンス")