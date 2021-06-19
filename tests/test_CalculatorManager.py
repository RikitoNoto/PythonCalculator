import os
import sys
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
sys.path.append(os.path.abspath(".."))

from src.CalculatorManager import CalculatorManager
from src.GUIManager import GUIManager
from src.Calculator import Calculator
from src.GUI.SendCharacters import SendCharacters


class CalculatorManagerTest(unittest.TestCase):
    CALCULATOR_MODULE_PATH = "src.CalculatorManager.Calculator"

    @patch("src.CalculatorManager.GUIManager", spec=GUIManager)
    def setUp(self, gui_stub:MagicMock) -> None:
        self.__manager = CalculatorManager()
        self.__gui_stub:MagicMock = gui_stub

    def main_display_check(self, text):
        try:
            self.assertEqual(self.__gui_stub.return_value.main_string, text)
        except AssertionError:
            self.__gui_stub.return_value.output_main.assert_called_with(text)

    @patch(CALCULATOR_MODULE_PATH, spec=Calculator)
    def create_calculator(self, calculator_stub)->MagicMock:
        """
        仮で__calculatorメンバの宣言を行うメソッドを呼び出しする。
        """
        self.__manager.num_event_handler(SendCharacters.ZERO)
        self.__manager.op_event_handler(SendCharacters.PLUS)
        return calculator_stub

    def input_value_by_num_event(self, value, operation=SendCharacters.PLUS):
        """
        引数で受け取った数値を頭から順にイベントとして呼び出しをし、最後にオペレータイベントを実行する。
        """
        for char in SendCharacters.consts(value):
            self.__manager.num_event_handler(char)
        if operation:
            self.__manager.op_event_handler(operation)

    def test_when_equal_event_call_calculate(self):
        """
        イコールボタンが押下された時に計算処理が呼び出されること
        """
        calculator_stub = self.create_calculator()
        self.__manager.eq_event_handler(SendCharacters.EQUAL)
        calculator_stub.return_value.calculate.assert_called_with()

    def test_after_equal_event_output_display(self):
        """
        計算結果を出力できているか。
        """
        output = "230974"
        calculator_stub = self.create_calculator()
        calculator_stub.return_value.calculate.return_value = output#Calculateメソッドの返り値をoutputに変更
        self.__manager.eq_event_handler(SendCharacters.EQUAL)
        self.main_display_check(output)

    @patch(CALCULATOR_MODULE_PATH, spec=Calculator)
    def test_when_operator_event_create_left_value(self, calculator_stub:MagicMock):
        """
        operator入力イベントが実行された時にleft_valueが正しく生成されているか。
        """
        self.__manager.num_event_handler(SendCharacters.FIVE)
        self.__manager.op_event_handler(SendCharacters.MINUS)
        try:
            self.assertEqual(calculator_stub.return_value.left_value, 5)
        except AssertionError:
            calculator_stub.assert_called_with(5)

    @patch(CALCULATOR_MODULE_PATH, spec=Calculator)
    def test_should_be_able_to_create_value(self, calculator_stub:MagicMock):
        """
        num入力イベントが入力された時に正しくvalueを組み立てられているか。
        """
        value = 356
        self.input_value_by_num_event(value)

        calculator_stub.assert_called_with(value)

    @patch(CALCULATOR_MODULE_PATH, spec=Calculator)
    def test_should_be_able_to_create_decimal(self, calculator_stub: MagicMock):
        """
        num入力イベントが入力された時に正しく小数点を含むvalueを組み立てられているか。
        """
        value = 356.134
        self.input_value_by_num_event(value)

        calculator_stub.assert_called_with(value)

    def test_when_operator_event_registe_operator(self):
        """
        operator入力イベントが実行された時にオペレータを正しく登録できているか。
        """
        plus = Calculator.PLUS

        with patch(self.CALCULATOR_MODULE_PATH, spec=Calculator) as calculator_stub:
            self.__manager.op_event_handler(SendCharacters.PLUS)
            self.assertEqual(calculator_stub.operator, plus)

if __name__ == '__main__':
    unittest.main()
