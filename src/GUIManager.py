from kivy.clock import Clock
from kivy.core.window import Window
try:
    from .GUI.SendCharacters import SendCharacters
    from .GUI.CalculatorApp import CalculatorApp as GuiApp
except (ModuleNotFoundError, ImportError):
    from GUI.SendCharacters import SendCharacters
    from GUI.CalculatorApp import CalculatorApp as GuiApp

class GUIManager(SendCharacters):
    '''
    GUIを管理するためのクラス。
    '''

    def __init__(self, event_num=None, event_op=None, event_eq=None, event_dec=None, event_ac=None):
        """
        初期化とアプリケーションクラスのインスタンス作成を行う。
        :param event_num: 数値ボタンが押下された時に実行するイベント
        :param event_op: 演算子ボタンが押下された時に実行するイベント
        :param event_eq: イコールボタンが押下された時に実行するイベント
        :param event_dec: 小数点ボタンが押下された時に実行するイベント
        :param event_ac: オールクリアボタンが押下された時に実行するイベント
        """
        self.__app = GuiApp(event_num=event_num, event_dec=event_dec, event_op=event_op, event_eq=event_eq, event_ac=event_ac)

    def output_main(self, text:str):
        """
        メインディスプレイへ文字列の出力を行う。
        :param text: 出力する文字列
        """
        self.main_string = text

    def output_sub(self, text:str):
        """
        サブディスプレイへ文字列の出力を行う。
        :param text: 出力する文字列
        """
        self.sub_string = text

    def app_run(self):
        """
        アプリを開始する。
        """
        self.__app.run()

    def app_end(self):
        """
        アプリを終了する。
        """
        self.__app.stop()
        Window.close()

    @staticmethod
    def set_schedule_interval(func, interval):
        """
        アプリケーション開始からinterval秒間隔でfuncを実行する。
        :param func: 実行する関数
        :param interval: 定期実行する間隔
        """
        Clock.schedule_interval(func, interval)

    @staticmethod
    def set_schedule_once(func, after):
        """
        アプリケーションの実行後、after秒後にfuncを実行する。
        :param func: 実行する関数
        :param after: アプリケーション開始からのオフセット時間
        """
        Clock.schedule_once(func, after)

    def get_main_string(self):
        return self.__app.widgets.main_string

    def set_main_string(self, text):
        self.__app.widgets.main_string = text

    def del_main_string(self):
        self.__app.widgets.main_string = ""

    def get_sub_string(self):
        return self.__app.widgets.sub_string

    def set_sub_string(self, text):
        self.__app.widgets.sub_string = text

    def del_sub_string(self):
        self.__app.widgets.sub_string = ""

    def set_event_num(self, handler):
        self.__app.event_num = handler

    def set_event_dec(self, handler):
        self.__app.event_dec = handler

    def set_event_op(self, handler):
        self.__app.event_op = handler

    def set_event_equal(self, handler):
        self.__app.event_equal = handler

    def set_event_ac(self, handler):
        self.__app.event_ac = handler


    main_string = property(get_main_string, set_main_string, del_main_string, "メイン表示部の文字列")
    """
    main_string
    メインディスプレイに表示している文字列
    """
    sub_string = property(get_sub_string, set_sub_string, del_sub_string, "サブ表示部の文字列")
    """
    サブディスプレイに表示している文字列
    """
    event_num = property(fset=set_event_num)
    """
    数値ボタンが押下された時に実行されるハンドラ
    """
    event_dec = property(fset=set_event_dec)
    """
    小数点ボタンが押下された時に実行されるハンドラ
    """
    event_op = property(fset=set_event_op)
    """
    演算子ボタンが押下された時に実行されるハンドラ
    """
    event_equal = property(fset=set_event_equal)
    """
    イコールボタンが押下された時に実行されるハンドラ
    """
    event_ac = property(fset=set_event_ac)
    """
    オールクリアボタンが押下された時に実行されるハンドラ
    """

if __name__ == '__main__':
    """
    テストプログラム
    ボタンを押下するとそれに対応した文字列がメインディスプレイに、
    一つ前に押したボタンがサブディスプレイに表示される。
    """
    from functools import partial
    gui = GUIManager()



    # def main_test(text, *args):
    #     gui.output_main(text)
    #
    # def sub_test(text, *args):
    #     gui.output_sub(text)
    #
    # gui.set_schedule_once(partial(main_test, "called"), 2)
    # gui.set_schedule_once(partial(sub_test, "called"), 3)

    def display_main(input):
        gui.output_sub(gui.main_string)
        gui.output_main(input)

    gui.event_num = display_main
    gui.event_dec = display_main
    gui.event_equal = display_main
    gui.event_ac = display_main
    gui.event_op = display_main

    gui.app_run()