
from unittest.main import main


class Calculator:

    def __init__(self, left_value):
        self.__leftvalue=left_value

    def calculate(self):
        pass
    def add(self):
        result=self.__left_value + self.__right_value
        return result

    def sub(self):
        pass

    def multi(self):
        pass

    def divi(self):
        pass



    @property
    def formula(self)->str:
        pass

    def get_left_value(self):
        return self.__leftvalue

    def set_left_value(self, value):
        self.__left_value=value

    def get_right_value(self):
        return self.__right_value

    def set_right_value(self, value):
        self.__right_value=value

    def get_operator(self): 
        return self.__operator

    def set_operator(self, op):
        self.__operator=op

    left_value = property(get_left_value, set_left_value)
    right_value = property(get_right_value, set_right_value)
    operator = property(get_operator, set_operator) #演算子 +-*/

if __name__ == '__main__':
    operator = 3
    def num ():
        return operator 

    print(num())




