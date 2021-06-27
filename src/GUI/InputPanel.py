import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window
from kivy.core.window import Keyboard

from SendCharacters import SendCharacters

class InputButton(Button):
    """
    入力ボタンのスーパークラス。
    """

    def link_button_on_press(self):
        """
        キーボードとリンクするためのメソッド
        実行すると、紐づけられたイベントを実行する。
        """
        self.dispatch("on_press")

    def link_button_on_release(self):
        """
        キーボードとリンクするためのメソッド
        実行すると、紐づけられたイベントを実行する。
        """
        self.dispatch("on_release")

class ButtonContainer(BoxLayout):
    """
    ボタンコンテナクラス。
    このクラスの中のボタンはキーボードと紐づけができる。
    """
    pass

class InputPanel(BoxLayout, SendCharacters):
    """
    入力パネルクラス。
    Buttonからの入力とキーボードからの入力を扱う。
    """
    Builder.load_file("{}/InputPanel.kv".format(os.path.dirname(__file__)))
    WITH_SHIFT = {Keyboard.keycodes[";"] : Keyboard.keycodes["+"],
                  Keyboard.keycodes[":"] : Keyboard.keycodes["*"],
                  Keyboard.keycodes["-"] : Keyboard.keycodes["enter"]}
    """
    シフトキーと同時押ししたときに変化するキーの設定
    変更前のキー : 変更後のキー
    の構文で記載する。
    """

    SIMPLE_COMVERT = {Keyboard.keycodes["numpad0"] : Keyboard.keycodes["0"],
                      Keyboard.keycodes["numpad1"] : Keyboard.keycodes["1"],
                      Keyboard.keycodes["numpad2"] : Keyboard.keycodes["2"],
                      Keyboard.keycodes["numpad3"] : Keyboard.keycodes["3"],
                      Keyboard.keycodes["numpad4"] : Keyboard.keycodes["4"],
                      Keyboard.keycodes["numpad5"] : Keyboard.keycodes["5"],
                      Keyboard.keycodes["numpad6"] : Keyboard.keycodes["6"],
                      Keyboard.keycodes["numpad7"] : Keyboard.keycodes["7"],
                      Keyboard.keycodes["numpad8"] : Keyboard.keycodes["8"],
                      Keyboard.keycodes["numpad9"] : Keyboard.keycodes["9"],
                      Keyboard.keycodes["numpaddivide"] : Keyboard.keycodes["/"],
                      Keyboard.keycodes["numpadmul"] : Keyboard.keycodes["*"],
                      Keyboard.keycodes["numpadsubstract"] : Keyboard.keycodes["-"],
                      Keyboard.keycodes["numpadadd"] : Keyboard.keycodes["+"],
                      Keyboard.keycodes["numpadenter"] : Keyboard.keycodes["enter"]}
    """
    単体で押下したときに変化するキーの設定
    変更前のキー : 変更後のキー
    の構文で記載する。
    """

    key_codes = Keyboard.keycodes#FIXME　kvファイル内で使用するために使用。kvファイルでKeyboardをインポートしてkeycodesを使用することができなかった。

    def __init__(self, *args, **kwargs):
        """
        キーボードイベントのバインドとプライベート変数の初期化
        """
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, input_type="text")
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

        self.__app = App.get_running_app()#アプリケーションの取得
        self.__shift = False#シフトボタンが押されているかのフラグ
        self.__ctrl = False#コントロールボタンが押されているかのフラグ

        super().__init__(*args, **kwargs)#スーパークラスの初期化

    def _keyboard_closed(self):
        """
        キーボードの接続解除イベントハンドラ
        """
        self._keyboard.unbind(on_key_down=self._on_keyboard_down, on_key_up=self._on_keyboard_up)
        self._keyboard = None

    def _on_keyboard_up(self, keyboard, keycode):
        """
        キーボードのボタンの立ち上がりに対するイベントハンドラ
        シフトとコントロールの監視をし、内部メソッドを実行する。
        """
        if(keycode[0] == Keyboard.keycodes["shift"] or keycode[0] == Keyboard.keycodes["rshift"]):
            self.__shift = False
        if(keycode[0] == Keyboard.keycodes["lctrl"] or keycode[0] == Keyboard.keycodes["rctrl"]):
            self.__ctrl = False
        self._button_on_release(keycode)

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        """
        キーボードのボタンの押下時に対するイベントハンドラ
        シフトとコントロールの監視をし、内部メソッドを実行する。
        """
        if(keycode[0] == Keyboard.keycodes["shift"] or keycode[0] == Keyboard.keycodes["rshift"]):
            self.__shift = True
        if(keycode[0] == Keyboard.keycodes["lctrl"] or keycode[0] == Keyboard.keycodes["rctrl"]):
            self.__ctrl = True
        self._button_on_press(keycode)

    def _button_on_press(self, keycode):
        """
        キーボード押下時のイベントハンドラ
        受け取ったキーコードがそれぞれのボタンに設定されているキーコードと一致したときに
        そのボタンを押下する。
        :param keycode: 押されたキーのキーコード
        """
        button = self.__get_event_button(keycode)
        if(button):
            button.state = "down"
            button.link_button_on_press()

    def _button_on_release(self, keycode):
        """
        キーボードの立ち上がりのイベントハンドラ
        受け取ったキーコードがそれぞれのボタンに設定されているキーコードと一致したときに
        そのボタンを離す。
        :param keycode: 離されたキーのキーコード
        """
        button = self.__get_event_button(keycode)
        if(button):
            button.state = "normal"
            button.link_button_on_release()

    def __get_event_button(self, keycode:list)->Widget:
        """
        配下のボタンクラスを検索し、受け取ったキーコードの情報を持つボタンを返す。
        :param keycode: 検索するキーコード
        :return: 引数で受け取ったキーコードを持つボタン
        """
        __keycode = self.__convert_key_code(keycode)
        return self.__search_button(__keycode, self)

    def __search_button(self, keycode, parent:Widget)->(Widget, None):
        """
        受け取ったウィジェットの中を検索し、引数と同じキーコードを持つウィジェットを返す。
        ウィジェットの中にButtonContainerクラスがいる場合は再帰的にこのメソッドを呼び出し検索する。
        :param keycode: 検索するキーコード
        :param parent: 検索するウィジェット
        :return: キーコードをもつウィジェット。いなければNone
        """
        for widget in parent.children:
            if(isinstance(widget, InputButton) and widget.keycode == keycode):
                return widget
            elif(isinstance(widget, ButtonContainer)):
                button = self.__search_button(keycode, widget)
                if(button):
                    return button
        return None


    def __convert_key_code(self, keycode: list)->int:
        """
        受けとったキーコードを定数の情報に沿って変換をし
        そのキーコードを返す。
        受け取るキーコードはキー名称とキーコードのリスト形式だが、返り値はキーコードのみの整数値。
        :param keycode: 変換前のキーコード
        :return: 変換後のキーコード
        """
        simple_convert = self.SIMPLE_COMVERT.get(keycode[0])
        if(simple_convert):
            return simple_convert

        shift_convert = self.WITH_SHIFT.get(keycode[0])

        if(self.__shift and shift_convert):
            return shift_convert
        return keycode[0]