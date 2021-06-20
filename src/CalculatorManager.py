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
    TODO: 数値　→　イコール　= 数値の表示
    TODO: 数値　→　オペレーター　→　数値　→　オペレーター　= 結果　&　leftvalue
    TODO: AC　→　クリア
    TODO: 前の値あり　→　イコール　=　前の値表示
    TODO: 前の値なし　→　イコール　=　0
    TODO: 前の値あり　→　オペレーター　=　前の値をleftvalueに代入
    TODO: 前の値なし　→　オペレーター　=　0をleftvalueに代入
    """
    OPERATOR_DICT = {
        SendCharacters.PLUS: Calculator.PLUS,
        SendCharacters.MINUS: Calculator.SUB,
        SendCharacters.MULTI: Calculator.MULTI,
        SendCharacters.DIVI: Calculator.DIVI
                     }


    def __init__(self):
        self.__gui = GUIManager(self.num_event_handler, self.op_event_handler, self.eq_event_handler)
        self.__reset_current_value()

    def run(self):
        self.__gui.app_run()

    def num_event_handler(self, input):
        self.__current_value += input
        self.__gui.output_main(str(self.__current_value))

    def op_event_handler(self, input):
        self.__calculator = Calculator(SendCharacters.to_num(self.__current_value))
        self.__calculator.operator = self.OPERATOR_DICT[input]
        self.__reset_current_value()

    def eq_event_handler(self, input):
        self.__calculator.right_value = SendCharacters.to_num(self.__current_value)
        self.__gui.output_main(str(self.__calculator.calculate()))
        self.__reset_current_value()

    def create_input_value(self):
        value = SendCharacters.to_num(self.__current_value)
        self.__reset_current_value()
        return value

    def __reset_current_value(self):
        self.__current_value = ""

if __name__ == '__main__':
    CalculatorManager().run()