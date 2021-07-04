from enum import IntEnum
from enum import auto

class Calculator:

    """
    定数指定
    0から3の数字に演算子を割り当てる

    101=: 1+1=
    111=: 1-1=
    121=: 1×1=
    131=: 1÷1=

    """
    class OPERATORS(IntEnum):
        PLUS = 0
        SUB  = auto()
        MULTI = auto()
        DIVI = auto()
        COUNT = auto()
    VALID_TYPE = (int, float, type(None))

    def __init__(self, left_value):
        """
        self.__left_valueにleft_valueを代入
        """
        self.__left_value = left_value
        self.__right_value = None

    def calculate(self): #TODO 0～3以外の数値が入ったら例外発生させる。後回し。
        """
        =押されたときに実行される
        計算結果を返す

        演算子に入っている値によって実行する式を変化させる
        
        例：operatorが0の時、左辺+右辺を実行してその結果を返す。

        0～3以外の値だった場合、例外発生させる。
        """

        if self.__right_value==None:
            """
            もしright_valueの値がNoneだったら
            opelate関係なく、left_valueの値を返す。
            """
            return self.left_value
            
            
        elif self.__operator==self.OPERATORS.PLUS:
            """
            もしself.__operatorが0だったら self.add()を実行して返す。
            """
            return self.add()

        elif self.__operator==self.OPERATORS.SUB:
            """
            もしself.__operatorが1だったら self.sub()を実行して返す。
            """
            return self.sub()

        elif self.__operator==self.OPERATORS.MULTI:
            """
            もしself.__operatorが2だったら self.multi()を実行して返す。
            """
            return self.multi()

        elif self.__operator==self.OPERATORS.DIVI:
            """
            もしself.__operatorが3だったら self.divi()を実行して返す。
            """
            return self.divi()
            
        else:
            return 


    def add(self):
        """
        self.__left_value(左辺)とself.__right_value(右辺)の値を足し算したものをresultに代入してresult返す。
        """

        return self.__left_value + self.__right_value

        
    def sub(self):
        """
        self.__left_value(左辺)とself.__right_value(右辺)の値を引き算したものをresultに代入してresult返す。
        """
        return self.__left_value - self.__right_value 
        

    def multi(self):
        """
        self.__left_value(左辺)とself.__right_value(右辺)の値を掛け算したものをresultに代入してresult返す。
        """
        return self.__left_value * self.__right_value


    def divi(self): #TODO __right_valueが0の時の例外補足クラス内に追加。0割が出たら"0 で割ることはできません"と文字列を返す。
        """
        self.__left_value(左辺)とself.__right_value(右辺)の値を割り算したものをresultに代入してresult返す。

        ※right_valueが0だったら
        """

        if self.__right_value==0:
            return "0 で割ることは出来ません。"

        else:
            return self.__left_value / self.__right_value
        
        # try:
        #      self.__right_value==0
        #     # return "0 で割ることはできません"

        # except:
        #     return "0 で割ることはできません"


    def operator_char(self): #TODO elseに例外を発生させること。operatorに違う値入ったら誤動作起きるので。後回し
        """
        現在のオペレータの値にあった文字を返す
        例：operetor=PLUS
        上記の時、"+"が返る
        """

        if self.__operator==self.OPERATORS.PLUS:
            """
            もしself.__operatorがself.PLUSだったら
            "+"を返す。
            """ 
            return "+"
                       
        elif self.__operator==self.OPERATORS.SUB:
            """
            もしself.__operatorがself.SUBだったら
            "-"を返す。
            """ 
            return "-"
            
        elif self.__operator==self.OPERATORS.MULTI:
            """
            もしself.__operatorがself.MULTIだったら
            "×を返す。
            """ 
            return "×"
            
        elif self.__operator==self.OPERATORS.DIVI:
            """
            もしself.__operatorがself.DIVIだったら
            "÷を返す。
            """ 
            return "÷"


        else: 
            """
            それ以外だったら
            エラー
            """ 
            return ""

    def index(self,digits): #TODO calculateを指数に変換する関数。
        """
        digitsに数値1が入った時、__digitsに".1E"が入るようにする。
        """
        __digits=digits    
        return format(self.calculate(),".{0}E".format(__digits)) 

    @property
    def formula(self)->str:    
        """
        str: 文字列に変換。

        例:
        str(self.__left_value)      :1 
        str(self.operator_char())   :0
        str(self.__right_value)     :1

        1+1を返す。※ =が押されたとき。
        """
        return "{0}{1}{2}".format(str(self.__left_value),str(self.operator_char()),str(self.__right_value or ""))

        # """
        
        # try: 右辺str(self.__right_value)の値がなかった場合、例外発生させる。
        # except: 右辺str(self.__right_value)の値がなくても動作させる。

        # """
        # try:
        #     return "{0}{1}{2}".format(str(self.__left_value),str(self.operator_char()),str(self.__right_value))

        # except AttributeError:
        #     return "{0}{1}".format(str(self.__left_value),str(self.operator_char()))
        
        

        # if self.__right_value==None:
        #     return "{0}{1}{2}".format(str(self.__left_value),str(self.operator_char()))

        # else:
        #     return "{0}{1}{2}".format(str(self.__left_value),str(self.operator_char()),str(self.__right_value))
        # # return  str(self.__left_value)+str(self.operator_char())+str(self.__right_value) 
        

    def get_left_value(self):

        """
        self.__left_valueを返す。
        """
        return self.__left_value

    def set_left_value(self, value):
        """
        もしleftvalueに数値以外の値を代入しようとしたときにエラー発生させる。
        """
        if(not isinstance(value, self.VALID_TYPE)):
            raise self.CalculatorValueError("左辺には数値しか代入できません。")
        self.__left_value=value


    def get_right_value(self):
        """
        self.__right_valueを返す。
        """
        return self.__right_value

    def set_left_value(self, value):
        """
        もしleftvalueに数値以外の値を代入しようとしたときにエラー発生させる。
        """
        if(not isinstance(value, self.VALID_TYPE)):
            raise self.CalculatorValueError("左辺には数値しか代入できません。")
        self.__left_value=value

    def get_right_value(self):
        """
        self.__right_valueを返す。
        """
        return self.__right_value

    def set_right_value(self, value):
        if(not isinstance(value, self.VALID_TYPE)):
            raise self.CalculatorValueError("右辺には数値しか代入できません。")
        self.__right_value=value

    def get_operator(self): 
        """
        self.__operatorを返す。
        """
        return self.__operator

    def set_operator(self, op):
        """ 
        self.__operatorにopを代入
        """
        if(op >= self.OPERATORS.COUNT):
            raise self.CalculatorValueError("存在しない演算子です。")
        self.__operator=op

    left_value = property(get_left_value, set_left_value)
    right_value = property(get_right_value, set_right_value)
    operator = property(get_operator, set_operator) #演算子 +-*/

    class CalculatorValueError(Exception):
        pass

if __name__ == '__main__':



    # result=Calculator(0)
    # result.left_value=2
    # result.right_value= None
    # result.operator=Calculator.OPERATORS.DIVI
    # print(result.calculate())

    # for a in range(10):
    #     print(result.index(a))
    
    # print(format(result.calculate(),'.1E'))
    # print(format(result.calculate(),'.2E'))
    # print(format(result.calculate(),'.3E'))
    # print(format(result.calculate(),'.4E'))
    # print(format(result.calculate(),'.5E'))
    # print(format(result.calculate(),'.6E'))
    # print(format(result.calculate(),'.7E'))
    # print(format(result.calculate(),'.8E'))
    # print(format(result.calculate(),'.9E'))
    # print(format(result.calculate(),'.10E'))



    calcu = Calculator(0)
    calcu.left_value = 1
    calcu.right_value = None
    calcu.operator = Calculator.OPERATORS.DIVI
    print(calcu.formula)
    

    # operator = 3
    # def num ():
    #     return operator 

    # print(num())


#TODO sphinxドキュメント出力できるようにコメント追加。
#TODO 指数(index)表記ができるようにcalculateメソッドの指数を返すパターン作成。
#TODO masterブランチ コンフリクト解消。後回し。
