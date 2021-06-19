from typing import Union
try:
    from GUIManager import GUIManager
    from Calculator import Calculator
except ModuleNotFoundError:
    from .GUIManager import GUIManager
    from .Calculator import Calculator

class CalculatorManager:

    def __init__(self):
        self.__gui = GUIManager(self.num_event_handler, self.op_event_handler, self.eq_event_handler)
        self.__current_value = ""

    def num_event_handler(self, input):
        self.__current_value += input

    def op_event_handler(self, input):
        self.__calculator = Calculator(self._create_value_from_string(self.__current_value))

    def eq_event_handler(self, input):
        self.__gui.output_main(self.__calculator.calculate())

    def _create_value_from_string(self, value_text)->Union[int, float]:
        if "." in value_text:
            return float(value_text)
        else:
            return int(value_text)

if __name__ == '__main__':
    pass