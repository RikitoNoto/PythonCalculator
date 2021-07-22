try:
    from CalculatePhase_if import CalculatePhase_if
    from CalculatePhaseTemplate_ab import CalculatePhaseTemplate_ab

except ModuleNotFoundError:
    from .CalculatePhase_if import CalculatePhase_if
    from .CalculatePhaseTemplate_ab import CalculatePhaseTemplate_ab

class RightValuePhase(CalculatePhaseTemplate_ab):

    def _initialize(self):
        super()._initialize()
        self._initial_phase = None
        self._operator_phase = None

    def push_number(self, input):
        return self

    def push_operator(self, input):
        return self.__get_operator_phase()

    def push_equal(self, input):
        return self.__get_initial_phase()

    def push_ac(self, input):
        return self.__get_initial_phase()

    def __get_initial_phase(self)->CalculatePhase_if:
        if self._initial_phase is None:
            try:
                from LeftValuePhase import LeftValuePhase as InitialPhase
            except ModuleNotFoundError:
                from .LeftValuePhase import LeftValuePhase as InitialPhase
            self._initial_phase = InitialPhase.get_instance()
        return self._initial_phase

    def __get_operator_phase(self)->CalculatePhase_if:
        if self._operator_phase is None:
            try:
                from OperatorPhase import OperatorPhase as OperatorPhase
            except ModuleNotFoundError:
                from .OperatorPhase import OperatorPhase as OperatorPhase
            self._operator_phase = OperatorPhase.get_instance()
        return self._operator_phase
