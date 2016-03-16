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
        # Ratio setting
        self.ratio = 0.9            # Ratio value for V*t/x < 1

        # Field variabels
        self.velocity = None          # Velocity [Lunit/Tunit]
        self._velocity = None         # Internal
        self.flow_distance = None     # Distance of flow travel [Lunit]
        self._flow_distance = None    # Internal

        # Time variabels
        self.delta_t = None          # Time delta [Tunit]
        self._delta_t = None         # Internal
        self.time_interval = None    # Simulation time interval [Tunit]
        self._time_interval = None   # Internal
        self.time_steps = None       # Number of steps in interval []
        self._time_steps = None      # Internal

        # Grid variabels
        self.delta_x = None          # Distance delta [Lunit]
        self._delta_x = None         # Internal
        self.reference_length = None # Reference length [Lunit]
        self._reference_length = None# Internal
        self.number_of_nodes = None  # Num nodes along reference []
        self._number_of_nodes = None # Internal

        return super(Freestream, self).__init__()

    """Different variabel calculations.    
        # Values should be defined as floats
        # Add error handling
    """
    # velocity
    # Calculate velocity from delta_t and delta_x
    def _calc_velocity_deltas(self):
        self._velocity = self.ratio*(self._delta_x/self._delta_t)

    # Calculate velocity from flow distance and time interval

    # delta_t
    # Calculate delta_t from time interval and number of steps
    def _calc_delta_t_from_time_and_steps(self):
        self._delta_t = self._time_interval/self._time_steps

    # Caluclate delta_t from velocity and delta_x
    def _calc_delta_t_from_velocity(self):
        self._delta_t = self._delta_x/self._velocity

    # delta_x
    # Calculate delta_x from reference length and number of nodes

    # Calculate delta_x from velocity and delta_t
    
    # time_interval
    # Calculate time from flow distance and velocity
    def _calc_time_from_flow_distance(self):
        self._time_interval = self._flow_distance/self._velocity

    # Calculate time from delta_t and number of steps
    
    # time_steps
    # Calculate number of steps from delta_t and time interval
       
    # ref_length
    # Calculate ref_length from delta_x and number of nodes

    # number_of_nodes
    # Calculate number_of_nodes from delta_X and reference length 