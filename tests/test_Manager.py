import unittest
import os
import sys

sys.path.append(os.path.abspath("../src"))

try:
    from Manager_if import Manager_if
    from CalculatorManager import CalculatorManager
    from SendCharacters import SendCharacters

except ModuleNotFoundError:
    from .Manager_if import Manager_if
    from .CalculatorManager import CalculatorManager
    from .SendCharacters import SendCharacters


class ManagerTest(unittest.TestCase):

    def test_should_be_create_leftvalue_when_push_number(self):
        manager:Manager_if = CalculatorManager()
        manager.push_number(SendCharacters.EIGHT)
        self.assertEqual(manager.current_value, "8")


if __name__ == '__main__':
    unittest.main()
