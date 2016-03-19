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
        # _ratio setting
        self._ratio = 0.9            # _ratio value for V*t/x < 1

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


    def __str__(self):
        ret_string = "Current Freestream values\n"
        ret_string = ret_string +"Velocity: " +str(self.get_velocity()) +"\n"       
        ret_string = ret_string +"Flow distance: " +str(self.get_flow_distance()) +"\n"  
        ret_string = ret_string +"Delta t: " +str(self.get_delta_t()) +"\n"  
        ret_string = ret_string +"Time interval: " +str(self.get_time_interval()) +"\n"  
        ret_string = ret_string +"Time steps: " +str(self.get_time_steps()) +"\n"  
        ret_string = ret_string +"Delta x: " +str(self.get_delta_x()) +"\n"  
        ret_string = ret_string +"Reference length: " +str(self.get_reference_length()) +"\n"  
        ret_string = ret_string +"Number of nodes: " +str(self.get_number_of_nodes()) +"\n"  
        return ret_string

    """Define all setters and getters to make updating values easier.
    """
    # velocity
    def set_velocity(self, velocity, internal=False):
        self._velocity_ = float(velocity)
        if internal is False:
            self._velocity = self._velocity_
        self._velocity_updated()

    def get_velocity(self):
        if self._velocity_:
            return self._velocity_
        else:
            return 0.0
    
    # flow_distance
    def set_flow_distance(self, flow_distance, internal=False):
        self._flow_distance_ = float(flow_distance)
        if internal is False:
            self._flow_distance = self._flow_distance_
        self._flow_distance_update()

    def get_flow_distance(self):
        if self._flow_distance_:
            return self._flow_distance_
        else:
            return 0.0

    # delta_t
    def set_delta_t(self, delta_t, internal=False):
        self._delta_t_ = float(delta_t)
        if internal is False:
            self._delta_t = self._delta_t_
        self._delta_t_updated()

    def get_delta_t(self):
        if self._delta_t_:
            return self._delta_t_
        else:
            return 0.0

    # time_interval
    def set_time_interval(self, time_interval, internal=False):
        self._time_interval_ = float(time_interval)
        if internal is False:
            self._time_interval = self._time_interval_
        self._time_interval_updated()

    def get_time_interval(self):
        if self._time_interval_:
            return self._time_interval_
        else:
            return 0.0

    # time_steps
    def set_time_steps(self, time_steps, internal=False):
        self._time_steps_ = float(time_steps)
        if internal is False:
            self._time_steps = self._time_steps_
        self._time_step_updated()

    def get_time_steps(self):
        if self._time_steps_:
            return self._time_steps_
        else:
            return 0.0

    # delta_x
    def set_delta_x(self, delta_x, internal=False):
        self._delta_x_ = float(delta_x)
        if internal is False:
            self._delta_x = self._delta_x_
        self._delta_x_updated()

    def get_delta_x(self):
        if self._delta_x_:
            return self._delta_x_
        else:
            return 0.0

    # reference_length
    def set_reference_length(self, reference_length, internal=False):
        self._reference_length_ = float(reference_length)
        if internal is False:
            self._reference_length = self._reference_length_
        self._reference_length_updated()

    def get_reference_length(self):
        if self._reference_length_:
            return self._reference_length_
        else:
            return 0.0

    # number_of_nodes
    def set_number_of_nodes(self, number_of_nodes, internal=False):
        self._number_of_nodes_ = float(number_of_nodes)
        if internal is False:
            self._number_of_nodes = self._number_of_nodes_
        self._number_of_nodes_updated()

    def get_number_of_nodes(self):
        if self._number_of_nodes_:
            return self._number_of_nodes_
        else:
            return 0.0

    """Functions caled when value is updated to update all possible
    resulting value changes.
    """
    # velocity
    def _velocity_updated(self):
        print("Velocity updated")
        # delta_t from delta_x
        if self._delta_x_ and not self._delta_t_:
            self.set_delta_t(self._calc_delta_t_from_velocity_(), True)
        # delta_x from delta_t
        elif self._delta_t_ and not self._delta_x_:
            self.set_delta_x(self._calc_delta_x_from_velocity_(), True)
        # flow_distance from time_interval
        elif self._flow_distance_ and not self._time_interval_:
            self.set_time_interval(self._calc_time_from_flow_distance_(), True)
        # time_interval from flow_distance
        elif self._time_interval_ and not self._flow_distance_:
            self.set_flow_distance(self._calc_flow_distance_from_velocity(), True)

    # flow_distance
    def _flow_distance_update(self):
        print("Flow distance updated")
        # time_interval from velocity
        if self._velocity_ and not self._time_interval_:
            self.set_time_interval(self._calc_time_from_flow_distance_(), True)
        # velocity from time_interval
        elif self._time_interval_ and not self._velocity_:
            self.set_velocity(self._calc_velocity_from_distance(), True)

    # delta_t
    def _delta_t_updated(self):
        print("Delta t updated")
        # velocity from delta_x
        if self._delta_x_ and not self._velocity_:            
            self.set_velocity(self._calc_velocity_from_deltas(), True)
        # delta_x from velocity
        elif self._velocity_ and not self._delta_x_:
            self.set_delta_x(self._calc_delta_x_from_velocity_(), True)
        # time_interval from time_steps
        elif self._time_steps_ and not self._time_interval_:
            self.set_time_interval(self._calc_time_from_delta_t_(), True)
        # time_steps from time_interval
        elif self._time_interval_ and not self._time_steps_:
            self.set_time_steps(self._calc_steps_from_delta_t_(), True)

    # delta_x
    def _delta_x_updated(self):
        print("Delta x updated")
        # velocity from delta_t
        if self._delta_t_ and not self._velocity_:            
            self.set_velocity(self._calc_velocity_from_deltas(), True)
        # delta_t from velocity
        elif self._velocity_ and not self._delta_t_:
            self.set_delta_t(self._calc_delta_t_from_velocity_(), True)
        # reference_length from number_of_nodes
        elif self._number_of_nodes_ and not self._reference_length_:
            self.set_reference_length(self._calc_ref_length_from_delta_x_(), True)
        # number_of_nodes from reference_length
        elif self._reference_length_ and not self._number_of_nodes_:
            self.set_number_of_nodes(self._calc_num_nodes_from_delta_x_(), True)

    # time_interval
    def _time_interval_updated(self):
        print("Time interval updated")
        # delta_t from time_step
        if self._time_steps_ and not self._delta_t_:
            self.set_delta_t(self._calc_delta_t_from_time_and_steps(), True)
        # time_step from delta_t
        elif self._delta_t_ and not self._time_steps_:
            self.set_time_steps(self._calc_steps_from_delta_t_(), True)
        # velocity from flow_distance
        elif self._flow_distance_ and not self._velocity_:
            self.set_velocity(self._calc_velocity_from_distance(), True)
        # flow_distance from velocity
        elif self._velocity_ and not self._flow_distance_:
            self.set_flow_distance(self._calc_flow_distance_from_velocity(), True)

    # time_step
    def _time_step_updated(self):
        print("Time step updated")
        # delta_t from time_interval
        if self._time_interval_ and not self._delta_t_:
            self.set_delta_t(self._calc_delta_t_from_time_and_steps(), True)
        # time_interval from delta_t
        elif self._delta_t_ and not self._time_interval_:
            self.set_time_steps(self._calc_time_from_delta_t_(), True)

    # reference_length
    def _reference_length_updated(self):
        print("Reference length updated")
        # delta_x from number_of_nodes
        if self._number_of_nodes_ and not self._delta_x_:
            self.set_delta_x(self._calc_delta_x_from_length(), True)
        # number_of_nodes from delta_x
        elif self._delta_x_ and not self._number_of_nodes_:
            self.set_number_of_nodes(self._calc_num_nodes_from_delta_x_(), True)

    # number_of_nodes
    def _number_of_nodes_updated(self):
        print("Number of nodes updated")
        # delta_x from reference_length
        if self._reference_length_ and not self._delta_x_:
            self.set_delta_x(self._calc_delta_x_from_length(), True)
        # reference_length from delta_x
        elif self._delta_x_ and not self._reference_length_:
            self.set_reference_length(self._calc_ref_length_from_delta_x_(), True)

    """Different variabel calculations.    
        # Values should be defined as floats
        # Add error handling
    """
    # velocity
    # Calculate velocity from delta_t and delta_x
    def _calc_velocity_from_deltas(self):
        return self._ratio*(self._delta_x_/self._delta_t_)

    # Calculate velocity from flow distance and time interval
    def _calc_velocity_from_distance(self):
        return self._flow_distance_/self._time_interval_

    # flow_distance
    # Calculate flow_distance from velocity and time interval
    def _calc_flow_distance_from_velocity(self):
        return self._velocity_*self._time_interval_

    # delta_t
    # Calculate delta_t from time interval and number of steps
    def _calc_delta_t_from_time_and_steps(self):
        return self._time_interval_/self._time_steps_

    # Caluclate delta_t from velocity and delta_x
    def _calc_delta_t_from_velocity_(self):
        return self._ratio*(self._delta_x_/self._velocity_)

    # delta_x
    # Calculate delta_x from reference length and number of nodes
    def _calc_delta_x_from_length(self):
        return self._reference_length_/self._number_of_nodes_

    # Calculate delta_x from velocity and delta_t
    def _calc_delta_x_from_velocity_(self):
        return (self._velocity_*self._delta_t_)/self._ratio
    
    # time_interval
    # Calculate time from flow distance and velocity
    def _calc_time_from_flow_distance_(self):
        return self._flow_distance_/self._velocity_

    # Calculate time interval from delta_t and number of steps
    def _calc_time_from_delta_t_(self):
        return self._delta_t_*self._time_steps_
    
    # time_steps
    # Calculate number of steps from delta_t and time interval
    def _calc_steps_from_delta_t_(self):
        return self._time_interval_/self._delta_t_
       
    # ref_length
    # Calculate ref_length from delta_x and number of nodes
    def _calc_ref_length_from_delta_x_(self):
        return self._delta_x_*self._number_of_nodes_

    # number_of_nodes
    # Calculate number_of_nodes from delta_x and reference length
    def _calc_num_nodes_from_delta_x_(self):
        return self._reference_length_/self._delta_x_

    """Actual workings.
    """
    # Reset all internal values for recalculation
    def _reset_internal_values(self):
        self._velocity_ = self._velocity
        self._flow_distance_ = self._flow_distance
        self._delta_t_ = self._delta_t
        self._time_interval_ = self._time_interval
        self._time_steps_ = self._time_steps
        self._delta_x_ = self._delta_x
        self._reference_length_ = self._reference_length
        self._number_of_nodes_ = self._number_of_nodes