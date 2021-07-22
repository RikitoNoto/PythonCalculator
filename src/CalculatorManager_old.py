from typing import Union
from enum import IntEnum
from enum import auto
try:
    from GUIManager import GUIManager
    from Calculator import Calculator
    from SendCharacters import SendCharacters
except ModuleNotFoundError:
    from .GUIManager import GUIManager
    from .Calculator import Calculator
    from .SendCharacters import SendCharacters

OPERATORS = Calculator.OPERATORS

class CalculatorManager:
    """
    guiの入力に対しての挙動を定義したクラス。
    """

    """
    GUIから送信されるメッセージをCalculatorクラスのオペレータに変換するためのdict
    """
    OPERATOR_DICT = {
        SendCharacters.PLUS: OPERATORS.PLUS,
        SendCharacters.MINUS: OPERATORS.SUB,
        SendCharacters.MULTI: OPERATORS.MULTI,
        SendCharacters.DIVI: OPERATORS.DIVI
                     }

    """
    起動時のメインディスプレイの表示文字列
    """
    MAIN_DISPLAY_INITIAL = "0"

    """
    起動時のサブディスプレイの表示文字列
    """
    SUB_DISPLAY_INITIAL = ""

    """
    ログの保持件数
    """
    HISTORY_BUFF = 100

    class PHASE(IntEnum):
        """
        現在の計算フェーズを表す列挙体
        """
        LEFT_VALUE = auto()     #左辺入力中
        OPERATOR = auto()       #演算子入力中
        RIGHT_VALUE = auto()    #右辺入力中
        EQUAL = auto()          #イコール処理中

    def __init__(self):
        """
        初期化。以下を行う。
        ・GUIインスタンスの作成、イベント登録
        ・インスタンス変数の初期化
        ・フェーズを左辺入力中に設定
        """
        self.__gui = GUIManager(event_num=self.num_event_handler, event_op=self.op_event_handler, event_eq=self.eq_event_handler, event_ac=self.ac_event_handler)
        self.__reset_current_value()
        self.__calculator = None
        self.__history = []
        self.__history_count = 0
        self.__phase = self.PHASE.LEFT_VALUE

    def run(self):
        """
        アプリを開始する。
        """
        self.__gui.app_run()
        self.gui_initialize()

    def gui_initialize(self):
        """
        GUIディスプレイの初期化を行う。
        """
        self.__gui.output_main(self.MAIN_DISPLAY_INITIAL)
        self.__gui.output_sub(self.SUB_DISPLAY_INITIAL)

    def num_event_handler(self, input):
        """
        数値ボタン押下時のイベントハンドラ。
        演算子入力前なら左辺の数値を作成。
        演算子入力後なら右辺の数値を作成。
        """
        if(self.__phase == self.PHASE.OPERATOR):
            self.__phase = self.PHASE.RIGHT_VALUE
        elif(self.__phase == self.PHASE.LEFT_VALUE):
            self.__gui.output_sub("")
        self.__current_value += SendCharacters.return_value(input)
        self.__gui.output_main(str(self.__current_value))

    def op_event_handler(self, input):
        """
        演算子ボタン押下時のイベントハンドラ。
        LeftValueフェーズならCalculatorインスタンスの作成。
        Operatorフェーズなら演算子の変更。
        """
        if(self.__phase == self.PHASE.LEFT_VALUE):
            """
            現在のフェーズがLeftValueなら
            """
            self.__phase = self.PHASE.OPERATOR#フェーズをOperatorに変更
            if(self.__is_inputed_number()):#数値が入力されているなら
                self.__calculator = Calculator(self.create_input_value())#入力されている数値を引数にCalculatorインスタンスの作成
            else:#数値が入力されていない状態で演算子ボタンが押下されたら
                self.__calculator = Calculator(0) if self.__history_count == 0 else Calculator(self.history_que(0).calculate())
                #ログデータがあれば最新ログを引数に、なければ0を引数にしてCalculatorインスタンスを作成

        elif(self.__phase == self.PHASE.RIGHT_VALUE):
            """
            現在のフェーズがRightValueなら
            """
            self.eq_event_handler(SendCharacters.EQUAL)#計算を実行
            return self.op_event_handler(input)#再起的に演算子ボタンを押下(ログを左辺としてオペレータメソッドを実行する)

        self.__calculator.operator = self.OPERATOR_DICT[input]#オペレータを代入
        self.__gui.output_sub(self.__calculator.formula)#計算式をサブディスプレイに出力
        self.__reset_current_value()#現在入力中の値をリセット

    def eq_event_handler(self, input):
        """
        イコールボタン押下時のイベントハンドラ
        数値が入力されていてRightValueフェーズならright_valueを代入後計算処理を実行する。
        LeftValueフェーズならログを引数にCalculatorインスタンスを作成し、計算処理を実行する。
        その他の場合はそのまま計算処理に移行する。(Operatorフェーズの場合はそのままright_valueに値をNoneで実行)

        計算実行後、計算結果をメインディスプレイに表示し計算式をサブディスプレイに表示する。
        その後フェーズをLeftValueへ戻す。
        """
        if self.__is_inputed_number() and self.__phase == self.PHASE.RIGHT_VALUE:
            """
            フェーズがRightValueで数値が入力されていたら
            """
            self.__calculator.right_value = self.create_input_value()#right_valueを代入

        elif self.__phase == self.PHASE.LEFT_VALUE:
            """
            フェーズがLeftValueなら
            """
            if self.__is_inputed_number():#数値が入力されているなら
                self.__calculator = Calculator(self.create_input_value())#入力値でCalculatorインスタンス作成
            else:#数値が入力されていなければ
                self.__calculator = Calculator(self.history_que(0).calculate()) if self.__history_count > 0 else Calculator(0)
                #ログがあればログで、なければ0でCalculatorインスタンスの作成

        self.__phase = self.PHASE.EQUAL#フェーズをEqualへ移行
        self.__gui.output_main(str(self.__calculator.calculate()))#メイン画面に計算結果を出力
        self.__gui.output_sub(self.__calculator.formula)#サブディスプレイに計算式を出力
        self.__registe_history(self.__calculator, del_calculator=True)#ログを登録
        self.__phase = self.PHASE.LEFT_VALUE#フェーズをLeftValueへ戻して終了

    def ac_event_handler(self, input):
        """
        ACボタン押下時のイベント
        Calculatorインスタンスの削除をし
        フェーズをLeftValueへ戻す。
        """
        self.__calculator = None
        self.gui_initialize()
        self.__phase = self.PHASE.LEFT_VALUE

    def create_input_value(self):
        """
        現在値(文字列)から数値を出力し、現在値のリセットを行う。
        """
        value = SendCharacters.to_num(self.__current_value)
        self.__reset_current_value()
        return value

    def history_que(self, index)->Calculator:
        """
        計算履歴から指定されたindexのログを取り出す。
        indexは0から順に最新のログが入っている。
        """
        return self.__history[index]

    def __reset_current_value(self):
        """
        現在値をリセットする。
        """
        self.__current_value = ""

    def __registe_history(self, history:Calculator, del_calculator=True):
        """
        ログの登録をする。
        :param del_calculator: Trueの時に現在のCalculatorインスタンスの削除を行う。
        """
        self.__history.insert(0, history)
        self.__history_count += 1
        while self.__history_count > self.HISTORY_BUFF:
            self.__history.pop()
            self.__history_count -= 1

        if del_calculator:
            self.__calculator = None

    def __is_inputed_number(self)->bool:
        """
        数値入力がされている時にTrueを返す。
        """
        return self.__current_value is not ""

    def get_calculator(self):
        return self.__calculator

    """
    Calculatorインスタンス
    """
    calculator = property(get_calculator)

if __name__ == '__main__':
    CalculatorManager().run()