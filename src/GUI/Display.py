import os
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty

class Display(Widget):
    """
    ディスプレイクラス
    内部にラベルをもっており、そのラベルを操作するための
    font_size、textプロパティを持つ。
    """
    Builder.load_file("{}/Display.kv".format(os.path.dirname(__file__)))
    text = StringProperty("")#表示文字列
    font_size = NumericProperty(50)#ラベルのフォントサイズ
    DISPLAY_BACK_GROUND_COLOR = [0.871, 0.882, 0.8]
    MAIN_FONT_COLOR = [0, 0, 0]

    def display(self, message):
        """
        ディスプレイにmessageを表示する。
        :param message: 表示したい文字列
        """
        self.text = message

if __name__ == '__main__':
    from kivy.app import App
    class Test(App):
        def build(self):
            return Display()

    Test().run()
