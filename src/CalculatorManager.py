
try:
    from Manager_if import Manager_if
    from Calculator import Calculator
    from SendCharacters import SendCharacters
except ModuleNotFoundError:
    from .Manager_if import Manager_if
    from .Calculator import Calculator
    from SendCharacters import SendCharacters

class CalculatorManager(Manager_if):
    def __init__(self):
        self.__phase = None
        self.__current_value = ""

    def push_number(self, input):
        self.__current_value += SendCharacters.return_value(input)

    def push_operator(self, input):
        pass

    def push_equal(self, input):
        pass

    def push_ac(self, input):
        pass

    def append_current_value(self):
        pass

    def get_current_phase(self):
        return self.__phase

    def get_current_value(self):
        return self.__current_value


    calculator = property(doc="Calculatorインスタンス")
    gui = property(doc="GUIManagerインスタンス")
    history = property(doc="過去の計算結果のログ")
    current_phase = property(fget=get_current_phase, doc="現在のフェーズクラスインスタンス")
    current_value = property(fget=get_current_value, doc="現在ユーザーが入力中の値")