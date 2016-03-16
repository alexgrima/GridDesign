class Freestream(object):
    """Class representing the freestream variabels allowing grid
    design estimations to be made for a freestream case.
    """

    # Initialisation of the class
    def __init__(self):
        """Initialises the class setting all fields to 0 and
        all internat variabels to None.
        Internal variabel is always updated to field value and used in
        calculations. If field value is None the internal value can 
        still recieve a value through calculations.
        """
        # Field variabels
        self._velocity = None          # Velocity [Lunit/Tunit]
        self._velocity_ = None         # Internal
        self._flow_distance = None     # Distance of flow travel [Lunit]
        self._flow_distance_ = None    # Internal

        # Time variabels
        self._delta_t = None          # Time delta [Tunit]
        self._delta_t_ = None         # Internal
        self._time_interval = None    # Simulation time interval [Tunit]
        self._time_interval_ = None   # Internal
        self._time_steps = None       # Number of steps in interval []
        self._time_steps_ = None      # Internal

        # Grid variabels
        self._delta_x = None          # Distance delta [Lunit]
        self._delta_x_ = None         # Internal
        self._reference_length = None # Reference length [Lunit]
        self._reference_length_ = None# Internal
        self._number_of_nodes = None  # Num nodes along reference []
        self._number_of_nodes_ = None # Internal

        return super(Freestream, self).__init__()

    # Velocity set::get
    def set_velocity(self, velocity):
        self._velocity = velocity

    def get_velocity(self):
        return self._velocity_

    # Flow distance set::get
    def set_flow_distance(self, flow_distance):
        self._flow_distance = flow_distance