
class Calculator:

    def __init__(self, left_value):
        pass

    def calculate(self):
        pass

    @property
    def formula(self)->str:
        pass

    def get_left_value(self):
        pass

    def set_left_value(self, value):
        pass

    def get_right_value(self):
        pass

    def set_right_value(self, value):
        pass

    def get_operator(self):
        pass

    def set_operator(self, op):
        pass

    left_value = property(get_left_value, set_left_value)
    right_value = property(get_right_value, set_right_value)
    operator = property(get_operator, set_operator)