try:
    from CalculatePhase_if import CalculatePhase_if
    from CalculatePhaseTemplate_ab import CalculatePhaseTemplate_ab

except ModuleNotFoundError:
    from .CalculatePhase_if import CalculatePhase_if
    from .CalculatePhaseTemplate_ab import CalculatePhaseTemplate_ab

class OperatorPhase(CalculatePhaseTemplate_ab):

    def _initialize(self):
        super()._initialize()
        self._next_phase = None
        self._initial_phase = None

    def push_number(self, input):
        return self.__get_next_phase()


    def push_operator(self, input):
        return self


    def push_equal(self, input):
        return self.__get_initial_phase()


    def push_ac(self, input):
        return self

    def __get_next_phase(self)->CalculatePhase_if:
        if self._next_phase is None:
            try:
                from RightValuePhase import RightValuePhase as NextPhase
            except ModuleNotFoundError:
                from .RightValuePhase import RightValuePhase as NextPhase
            self._next_phase = NextPhase.get_instance()
        return self._next_phase

    def __get_initial_phase(self)->CalculatePhase_if:
        if self._initial_phase is None:
            try:
                from LeftValuePhase import LeftValuePhase as InitialPhase
            except ModuleNotFoundError:
                from .LeftValuePhase import LeftValuePhase as InitialPhase
            self._initial_phase = InitialPhase.get_instance()
        return self._initial_phase