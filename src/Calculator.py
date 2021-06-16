
from unittest.main import main


class Calculator:
    PLUS = 0 
    SUB  = 1
    MULTI = 2
    DIVI = 3

    def __init__(self, left_value):
        self.__left_value=left_value

    def calculate(self):
        """
        =押されたときに実行される
        計算結果を返す

        演算子に入っている値によって実行する式を変化させる
        
        例：operatorが0の時、左辺+右辺を実行してその結果を返す。
        """

        if self.__operator==0:
            return self.add()
        elif self.__operator==1:
            return self.sub()
        elif self.__operator==2:
            return self.multi()
        elif self.__operator==3:
            return self.divi()
        else:
            pass 


    def add(self):
        result=self.__left_value + self.__right_value
        return result

    def sub(self):
        result=self.__left_value - self.__right_value
        return result

    def multi(self):
        result=self.__left_value * self.__right_value
        return result

    def divi(self):
        result=self.__left_value / self.__right_value
        return result

    def operator_char(self):
        """
        現在のオペレータの値にあった文字を返す
        例：operetor=PLUS
        上記の時、"+"が返る
        """

        if self.__operator==self.PLUS:
            return "+"
        elif self.__operator==self.SUB:
            return "-"
        elif self.__operator==self.MULTI:
            return "×"
        else:
            return "÷"


    @property
    def formula(self)->str:
        return  str(self.__left_value)+str(self.operator_char())+str(self.__right_value)+"="
            
        

    def get_left_value(self):
        return self.__left_value

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

    calcu = Calculator(0)
    calcu.left_value = 1
    calcu.right_value =2
    calcu.operator = Calculator.PLUS
    print(calcu.formula)

    # operator = 3
    # def num ():
    #     return operator 

    # print(num())
