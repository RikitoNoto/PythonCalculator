try:
    from CalculatePhase_if import CalculatePhase_if

except ModuleNotFoundError:
    from .CalculatePhase_if import CalculatePhase_if

class RightValuePhase(CalculatePhase_if):

    def push_number(self, input):
        return self


    def push_operator(self, input):
        pass


    def push_equal(self, input):
        pass


    def push_ac(self, input):
        pass