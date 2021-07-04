from typing import Union
try:
    from GUIManager import GUIManager
    from Calculator import Calculator
    from SendCharacters import SendCharacters
except ModuleNotFoundError:
    from .GUIManager import GUIManager
    from .Calculator import Calculator
    from .SendCharacters import SendCharacters

class CalculatorManager:
    """
    guiの入力に対しての挙動を定義したクラス。
    """
    OPERATOR_DICT = {
        SendCharacters.PLUS: Calculator.PLUS,
        SendCharacters.MINUS: Calculator.SUB,
        SendCharacters.MULTI: Calculator.MULTI,
        SendCharacters.DIVI: Calculator.DIVI
                     }
    MAIN_DISPLAY_INITIAL = "0"
    SUB_DISPLAY_INITIAL = ""
    HISTORY_BUFF = 100

    def __init__(self):
        self.__gui = GUIManager(event_num=self.num_event_handler, event_op=self.op_event_handler, event_eq=self.eq_event_handler, event_ac=self.ac_event_handler)
        self.__reset_current_value()
        self.__calculator = None
        self.__history = []
        self.__history_count = 0

    def run(self):
        self.__gui.app_run()
        self.gui_initial()

    def gui_initial(self):
        """
        GUIの初期化処理
        """
        self.__gui.output_main(self.MAIN_DISPLAY_INITIAL)
        self.__gui.output_sub(self.SUB_DISPLAY_INITIAL)

    def num_event_handler(self, input):
        self.__current_value += SendCharacters.return_value(input)
        self.__gui.output_main(str(self.__current_value))

    def op_event_handler(self, input):
        if(self.__current_value == ""):
            if self.__history_count == 0:
                self.__calculator = Calculator(0)
            else:
                self.__calculator = Calculator(self.history_que(0).calculate())
        elif(self.__calculator and self.__calculator.right_value):
            self.eq_event_handler(SendCharacters.EQUAL)
            return self.op_event_handler(input)
        else:
            self.__calculator = Calculator(SendCharacters.to_num(self.__current_value))
        self.__calculator.operator = self.OPERATOR_DICT[input]
        self.__gui.output_sub(self.__calculator.formula)
        self.__reset_current_value()

    def eq_event_handler(self, input):
        if self.__current_value is not "":
            self.__calculator.right_value = SendCharacters.to_num(self.__current_value)

        if not self.__calculator:
            if self.__history_count == 0:
                self.__calculator = Calculator(0)
            else:
                self.__calculator = Calculator(self.history_que(0).calculate())
        self.__gui.output_main(str(self.__calculator.calculate()))
        self.__gui.output_sub(self.__calculator.formula)
        self.__registe_history(self.__calculator, del_calculator=True)
        self.__reset_current_value()

    def ac_event_handler(self, input):
        self.__calculator = None

    def create_input_value(self):
        value = SendCharacters.to_num(self.__current_value)
        self.__reset_current_value()
        return value

    def history_que(self, index)->Union[Calculator, None]:
        if self.__history_count > 0:
            return self.__history[index]
        else:
            return None

    def __reset_current_value(self):
        self.__current_value = ""

    def __registe_history(self, history:Calculator, del_calculator=True):
        self.__history.insert(0, history)
        self.__history_count += 1
        while self.__history_count > self.HISTORY_BUFF:
            self.__history.pop()
            self.__history_count -= 1

        if del_calculator:
            self.__calculator = None

    def get_calculator(self):
        return self.__calculator

    calculator = property(get_calculator)

if __name__ == '__main__':
    CalculatorManager().run()