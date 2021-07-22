import unittest
from ManagerStub import ManagerStub

import os
import sys
sys.path.append(os.path.abspath(".."))

from src.SendCharacters import SendCharacters
from src.CalculatorManager import CalculatorManager
from src.Manager_if import Manager_if

sys.path.append(os.path.abspath("../src/CalculatePhases"))

from CalculatePhase_if import CalculatePhase_if
from LeftValuePhase import LeftValuePhase
from OperatorPhase import OperatorPhase
from RightValuePhase import RightValuePhase

class PhaseSystemTest(unittest.TestCase):

    def assertEqualPhaseAfterPushNumber(self, current_phase:type(CalculatePhase_if), expect_phase:type(CalculatePhase_if), send_char=SendCharacters.ZERO):
        """
        数値ボタンを押したときに想定したフェーズに移行しているかのテスト
        """
        phase: CalculatePhase_if = current_phase.get_instance()
        self.assertIsInstance(phase.push_number(send_char), expect_phase)

    def assertEqualPhaseAfterPushOperator(self, current_phase:type(CalculatePhase_if), expect_phase:type(CalculatePhase_if), send_char=SendCharacters.PLUS):
        """
        演算子ボタンを押したときに想定したフェーズに移行しているかのテスト
        """
        phase: CalculatePhase_if = current_phase.get_instance()
        self.assertIsInstance(phase.push_operator(send_char), expect_phase)

    def assertEqualPhaseAfterPushEqual(self, current_phase:type(CalculatePhase_if), expect_phase:type(CalculatePhase_if), send_char=SendCharacters.EQUAL):
        """
        イコールボタンを押したときに想定したフェーズに移行しているかのテスト
        """
        phase: CalculatePhase_if = current_phase.get_instance()
        self.assertIsInstance(phase.push_equal(send_char), expect_phase)

    def assertEqualPhaseAfterPushAc(self, current_phase:type(CalculatePhase_if), expect_phase:type(CalculatePhase_if), send_char=SendCharacters.AC):
        """
        ACボタンを押したときに想定したフェーズに移行しているかのテスト
        """
        phase: CalculatePhase_if = current_phase.get_instance()
        self.assertIsInstance(phase.push_ac(send_char), expect_phase)

    def test_should_not_be_change_phase_when_push_number_in_left_phase(self):
        """
        LeftValueフェーズの時に数値ボタンが押下されてもフェーズが変わらないこと
        """
        self.assertEqualPhaseAfterPushNumber(LeftValuePhase, LeftValuePhase)

    def test_should_be_change_to_operator_when_push_operator_in_left_phase(self):
        """
        LeftValueフェーズの時に演算子ボタンが押下されるとOperatorフェーズへ変わること
        """
        self.assertEqualPhaseAfterPushOperator(LeftValuePhase, OperatorPhase)

    def test_should_be_not_change_phase_when_push_equal_in_left_phase(self):
        """
        LeftValueフェーズの時にイコールボタンが押下されるとLeftValueフェーズへ変わること(フェーズ上では変化のないこと)
        """
        self.assertEqualPhaseAfterPushEqual(LeftValuePhase, LeftValuePhase)

    def test_should_be_not_change_phase_when_push_ac_in_left_phase(self):
        """
        LeftValueフェーズの時にACボタンが押下されるとLeftValueフェーズへ変わること(フェーズ上では変化のないこと)
        """
        self.assertEqualPhaseAfterPushAc(LeftValuePhase, LeftValuePhase)

    def test_should_be_change_to_right_when_push_number_in_operator_phase(self):
        """
        Operatorフェーズの時に数値ボタンが押下されるとRightValueフェーズへ変わること
        """
        self.assertEqualPhaseAfterPushNumber(OperatorPhase, RightValuePhase)

    def test_should_not_be_change_phase_when_push_operator_in_operator_phase(self):
        """
        Operatorフェーズの時に演算子ボタンが押下されてもフェーズが変わらないこと
        """
        self.assertEqualPhaseAfterPushOperator(OperatorPhase, OperatorPhase)

    def test_should_be_change_to_left_when_push_equal_in_operator_phase(self):
        """
        Operatorフェーズの時にイコールボタンが押下されるとLeftValueフェーズへ変わること
        """
        self.assertEqualPhaseAfterPushEqual(OperatorPhase, LeftValuePhase)

    def test_should_not_be_change_phase_when_push_ac_in_operator_phase(self):
        """
        Operatorフェーズの時にACボタンが押下されるとOperatorフェーズへ変わること(フェーズ上では変化のないこと)
        """
        self.assertEqualPhaseAfterPushAc(OperatorPhase, OperatorPhase)

    def test_should_not_be_change_phase_when_push_number_in_right_phase(self):
        """
        RightValueフェーズの時に数値ボタンが押下されてもフェーズが変わらないこと
        """
        self.assertEqualPhaseAfterPushNumber(RightValuePhase, RightValuePhase)

    def test_should_be_change_to_operator_when_push_operator_in_right_phase(self):
        """
        RightValueフェーズの時に演算子ボタンが押下されるとOperatorValueフェーズへ変わること
        """
        self.assertEqualPhaseAfterPushOperator(RightValuePhase, OperatorPhase)

    def test_should_be_change_to_left_when_push_equal_in_right_phase(self):
        """
        RightValueフェーズの時にイコールボタンが押下されるとLeftValueフェーズへ変わること
        """
        self.assertEqualPhaseAfterPushEqual(RightValuePhase, LeftValuePhase)

    def test_should_be_change_to_left_when_push_ac_in_right_phase(self):
        """
        RightValueフェーズの時にACボタンが押下されるとLeftValueフェーズへ変わること
        """
        self.assertEqualPhaseAfterPushAc(RightValuePhase, LeftValuePhase)

if __name__ == '__main__':
    unittest.main()