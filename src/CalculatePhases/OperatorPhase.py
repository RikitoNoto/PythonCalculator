try:
    from CalculatePhase_if import CalculatePhase_if
    from LeftValuePhase import LeftValuePhase as InitialPhase
    from RightValuePhase import RightValuePhase as NextPhase

except ModuleNotFoundError:
    from .CalculatePhase_if import CalculatePhase_if
    from .LeftValuePhase import LeftValuePhase as InitialPhase
    from .RightValuePhase import RightValuePhase as NextPhase

class OperatorPhase(CalculatePhase_if):

    def push_number(self, input):
        return NextPhase.get_instance()


    def push_operator(self, input):
        return self


    def push_equal(self, input):
        return InitialPhase.get_instance()


    def push_ac(self, input):
        return self