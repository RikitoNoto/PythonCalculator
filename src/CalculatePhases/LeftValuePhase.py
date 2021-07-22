try:
    from CalculatePhase_if import CalculatePhase_if
    from OperatorPhase import OperatorPhase as NextPhase

except ModuleNotFoundError:
    from .CalculatePhase_if import CalculatePhase_if
    from .OperatorPhase import OperatorPhase as NextPhase

class LeftValuePhase(CalculatePhase_if):

    def push_number(self, input):
        return self


    def push_operator(self, input):
        return NextPhase.get_instance()


    def push_equal(self, input):
        return self


    def push_ac(self, input):
        return self
