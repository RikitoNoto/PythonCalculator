import os
import sys
import unittest
sys.path.append(os.path.abspath(".."))

from src.Calculator import Calculator


class CalculatorTest(unittest.TestCase):
    LEFT_VALUE = 4564#テスト用の左辺
    RIGHT_VALUE = 349#テスト用の右辺

    def setUp(self) -> None:
        self.create_calculator(self.LEFT_VALUE)
        self.calculator.right_value = self.RIGHT_VALUE


    def tearDown(self) -> None:
        pass

    def create_calculator(self, left_value):
        """
        calculatorインスタンスを作成し、インスタンス変数へ代入する
        :param left_value: 左辺
        :return:
        """
        self.calculator = Calculator(left_value)

    def substitution_left_right(self, left=LEFT_VALUE, right=RIGHT_VALUE):
        self.calculator.left_value = left
        self.calculator.right_value = right

    # @unittest.skip("write the code")
    def test_add_unit(self):
        """
        add関数の単体テスト
        """
        self.substitution_left_right()
        self.assertEqual(self.calculator.add(), self.LEFT_VALUE + self.RIGHT_VALUE)

    # @unittest.skip("write the code")
    def test_sub_unit(self):
        """
        sub関数の単体テスト
        """
        self.substitution_left_right()
        self.assertEqual(self.calculator.sub(), self.LEFT_VALUE - self.RIGHT_VALUE)

    # @unittest.skip("write the code")
    def test_multi_unit(self):
        """
        multi関数の単体テスト
        """
        self.substitution_left_right()
        self.assertEqual(self.calculator.multi(), self.LEFT_VALUE * self.RIGHT_VALUE)

    # @unittest.skip("write the code")
    def test_divi_unit(self):
        """
        divi関数の単体テスト
        """
        self.substitution_left_right()
        self.assertEqual(self.calculator.divi(), self.LEFT_VALUE / self.RIGHT_VALUE)

    # @unittest.skip("write the code")
    def test_add(self):
        """
        加算のテスト。
        :return:
        """
        self.calculator.operator=Calculator.PLUS #TODO 加算のオペレータを入力する処理
        self.assertEqual(self.calculator.calculate(), self.LEFT_VALUE + self.RIGHT_VALUE)

    # @unittest.skip("write the code")
    def test_sub(self):
        """
        減算のテスト
        :return:
        """
        self.calculator.operator=Calculator.SUB #TODO 減算のオペレータを入力する処理
        self.assertEqual(self.calculator.calculate(), self.LEFT_VALUE - self.RIGHT_VALUE)

    # @unittest.skip("write the code")
    def test_multi(self):
        """
        掛け算のテスト
        :return:
        """
        self.calculator.operator=Calculator.MULTI #TODO かけ算のオペレータを入力する処理
        self.assertEqual(self.calculator.calculate(), self.LEFT_VALUE * self.RIGHT_VALUE)

    # @unittest.skip("write the code")
    def test_divi(self):
        """
        割り算のテスト
        :return:
        """
        self.calculator.operator=Calculator.DIVI #TODO 割り算のオペレータを入力する処理
        self.assertEqual(self.calculator.calculate(), self.LEFT_VALUE / self.RIGHT_VALUE)

    # @unittest.skip("write the code")
    def test_formula_add(self):
        """
        足し算後の式が正しく受け取れるかのテスト
        :return:
        """
        self.test_add()
        self.assertEqual(self.calculator.formula, "{}+{}=".format(self.LEFT_VALUE, self.RIGHT_VALUE))

    # @unittest.skip("write the code")
    def test_formula_sub(self):
        """
        減算後の式が正しく受け取れるかのテスト
        :return:
        """
        self.test_sub()
        self.assertEqual(self.calculator.formula, "{}-{}=".format(self.LEFT_VALUE, self.RIGHT_VALUE))

    # @unittest.skip("write the code")
    def test_formula_multi(self):
        """
        掛け算後の式が正しく受け取れるかのテスト
        :return:
        """
        self.test_multi()
        self.assertEqual(self.calculator.formula, "{}×{}=".format(self.LEFT_VALUE, self.RIGHT_VALUE))

    # @unittest.skip("write the code")
    def test_formula_divi(self):
        """
        割り算後の式が正しく受け取れるかのテスト
        :return:
        """
        self.test_divi()
        self.assertEqual(self.calculator.formula, "{}÷{}=".format(self.LEFT_VALUE, self.RIGHT_VALUE))

    # @unittest.skip("write the code")
    def test_left_value(self):
        """
        左辺の代入が正しくできるかのテスト
        :return:
        """
        self.calculator.left_value = self.LEFT_VALUE
        self.assertEqual(self.calculator.left_value, self.LEFT_VALUE)

    # @unittest.skip("write the code")
    def test_right_value(self):
        """
        右辺の代入が正しくできるかのテスト
        :return:
        """
        self.calculator.right_value = self.RIGHT_VALUE
        self.assertEqual(self.calculator.right_value, self.RIGHT_VALUE)

    def test_invalid_value_in_left_value(self):
        """
        left_valueに無効な値が入っている時に正しく例外が発生すること
        """
        with self.assertRaises(Calculator.CalculatorValueError):
            self.calculator.left_value = "a"

    def test_invalid_value_in_right_value(self):
        """
        right_valueに無効な値が入っている時に正しく例外が発生すること
        """
        with self.assertRaises(Calculator.CalculatorValueError):
            self.calculator.right_value = "a"

if __name__ == '__main__':
    unittest.main()
