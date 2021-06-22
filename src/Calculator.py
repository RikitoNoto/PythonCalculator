
# from unittest.main import main

class Calculator:
    """
    定数指定
    0から3の数字に演算子を割り当てる

    101=: 1+1=
    111=: 1-1=
    121=: 1×1=
    131=: 1÷1=

    """
    PLUS = 0  #TODO 自動設定(autoメソッド)にしてスムーズに。 後回し。
    SUB  = 1
    MULTI = 2
    DIVI = 3
    VALID_TYPE = (int, float)

    def __init__(self, left_value):
        """
        self.__left_valueにleft_valueを代入
        """
        self.__left_value=left_value

    def calculate(self): #TODO 0～3以外の数値が入ったら例外発生させる。後回し。
        """
        =押されたときに実行される
        計算結果を返す

        演算子に入っている値によって実行する式を変化させる
        
        例：operatorが0の時、左辺+右辺を実行してその結果を返す。

        0～3以外の値だった場合、例外発生させる。
        """

        if self.__operator==self.PLUS: 
            return self.add()
            """
            もしself.__operatorが0だったら self.add()を実行して返す。
            """
        elif self.__operator==self.SUB:
            return self.sub()
            """
            もしself.__operatorが1だったら self.sub()を実行して返す。
            """
        elif self.__operator==self.MULTI:
            return self.multi()
            """
            もしself.__operatorが2だったら self.multi()を実行して返す。
            """   
        elif self.__operator==self.DIVI:
            return self.divi()
            """
            もしself.__operatorが3だったら self.divi()を実行して返す。
            """   
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

        return self.__left_value / self.__right_value


    def operator_char(self): #TODO elseに例外を発生させること。operatorに違う値入ったら誤動作起きるので。後回し
        """
        現在のオペレータの値にあった文字を返す
        例：operetor=PLUS
        上記の時、"+"が返る
        """

        if self.__operator==self.PLUS:
            """
            もしself.__operatorがself.PLUSだったら
            "+"を返す。
            """ 
            return "+"
                       
        elif self.__operator==self.SUB:
            """
            もしself.__operatorがself.SUBだったら
            "-"を返す。
            """ 
            return "-"
            
        elif self.__operator==self.MULTI:
            """
            もしself.__operatorがself.MULTIだったら
            "×を返す。
            """ 
            return "×"
            
        elif self.__operator==self.DIVI:
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

    def index(self): #TODO calculateを指数に変換する関数。
        




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


        try:
            return "{0}{1}{2}".format(str(self.__left_value),str(self.operator_char()),str(self.__right_value))

        except AttributeError:
            return "{0}{1}".format(str(self.__left_value),str(self.operator_char()))
            



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
        もし
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
        self.__operator=op

    left_value = property(get_left_value, set_left_value)
    right_value = property(get_right_value, set_right_value)
    operator = property(get_operator, set_operator) #演算子 +-*/

    class CalculatorValueError(Exception):
        pass

if __name__ == '__main__':

    calcu = Calculator(0)
    calcu.left_value = 1
    # calcu.right_value =
    calcu.operator = Calculator.PLUS
    print(calcu.formula)

    # operator = 3
    # def num ():
    #     return operator 

    # print(num())


#TODO sphinxドキュメント出力できるようにコメント追加。
#TODO 指数(index)表記ができるようにcalculateメソッドの指数を返すパターン作成。
#TODO masterブランチ コンフリクト解消。後回し。