class Freestream(object):
    """Class representing the freestream variabels allowing grid
    design estimations to be made for a freestream case.
    """

    def __init__(self):
        """Initialises the class setting all fields to 0 and
        all internat variabels to None.
        Internal variabel is always updated to field value and used in
        calculations. If field value is None the internal value can 
        still recieve a value through calculations.
        """
        # Field variabels
        _velocity = None          # Velocity [Lunit/Tunit]
        _velocity_ = None         # Internal
        _flow_distance = None     # Distance of flow travel [Lunit]
        _flow_distance_ = None    # Internal

        # Time variabels
        _delta_t = None          # Time delta [Tunit]
        _delta_t_ = None         # Internal
        _time_interval = None    # Simulation time interval [Tunit]
        _time_interval_ = None   # Internal
        _time_steps = None       # Number of steps in interval []
        _time_steps_ = None      # Internal

        # Grid variabels
        _delta_x = None          # Distance delta [Lunit]
        _delta_x_ = None         # Internal
        _reference_length = None # Reference length [Lunit]
        _reference_length_ = None# Internal
        _number_of_nodes = None  # Nummber of nodes along reference []
        _number_of_nodes_ = None # Internal


        return super(Freestream, self).__init__()


