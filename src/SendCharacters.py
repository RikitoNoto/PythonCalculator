from typing import Union
class SendCharacters:
    """
    ユーザーがボタンを押下したときにイベントハンドラに引数として送信される文字列
    """
    AC = "$"
    DIVI = "/"
    MULTI = "*"
    PLUS = "+"
    MINUS = "-"
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    ZERO = "0"
    DECIMAL = "."
    EQUAL = "="
    VALUE_DICT = {
            "0": ZERO,
            "1": ONE,
            "2": TWO,
            "3": THREE,
            "4": FOUR,
            "5": FIVE,
            "6": SIX,
            "7": SEVEN,
            "8": EIGHT,
            "9": NINE,
            ".": DECIMAL
        }

    @staticmethod
    def consts(value):
        """
        数値に対して、大きい桁から順に定数を返すジェネレーター
        """
        for char in str(value):
            if SendCharacters.VALUE_DICT[char]:
                yield SendCharacters.VALUE_DICT[char]
            else:
                raise ValueError("{}:数値用定数に存在しない値が渡されました。".format(char))

    @staticmethod
    def return_value(char)->Union[str, None]:
         """
         引数で受け取った定数に当たる数値を返す。
         """
         for value, const_char in SendCharacters.VALUE_DICT.items():
             if(char == const_char):
                 return value
         else:
             return None

    @staticmethod
    def to_num(value:str)->Union[int, float]:
        value_text = ""
        for char in str(value):
            value_text += SendCharacters.VALUE_DICT[char]
        if "." in value_text:
            return float(value_text)
        else:
            return int(value_text)