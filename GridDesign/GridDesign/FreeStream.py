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
        # ratio setting
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
        if self._velocity_ != velocity:
            print("Velocity changed")
            if velocity:
                self._velocity_ = float(velocity)
                print("-Checking velocity dependencies")
                self._velocity_updated()
            if internal is False:
                print("Velocity updated by user")
                self._velocity = velocity

    def get_velocity(self):
        if self._velocity_:
            return self._velocity_
        else:
            return 0.0

    def is_set_velocity(self):
        if self._velocity:
            return True
        else:
            return False
    
    # flow_distance
    def set_flow_distance(self, flow_distance, internal=False):
        if self._flow_distance_ != flow_distance:
            print("Flow distance changed")
            if flow_distance:
                self._flow_distance_ = float(flow_distance)
                print("-Checking flow distance dependencies")
                self._flow_distance_update()
            if internal is False:
                print("Flow distance updated by user")
                self._flow_distance = flow_distance

    def get_flow_distance(self):
        if self._flow_distance_:
            return self._flow_distance_
        else:
            return 0.0

    def is_set_flow_distance(self):
        if self._flow_distance:
            return True
        else:
            return False

    # delta_t
    def set_delta_t(self, delta_t, internal=False):
        if self._delta_t_ != delta_t:
            print("Delta t changed")
            if delta_t:
                self._delta_t_ = float(delta_t)
                print("-Checking delta t dependencies")
                self._delta_t_updated()
            if internal is False:
                print("Delta t updated by user")
                self._delta_t = delta_t

    def get_delta_t(self):
        if self._delta_t_:
            return self._delta_t_
        else:
            return 0.0

    def is_set_delta_t(self):
        if self._delta_t:
            return True
        else:
            return False

    # time_interval
    def set_time_interval(self, time_interval, internal=False):
        if self._time_interval_ != time_interval:
            print("Time interval changed")
            if time_interval:
                self._time_interval_ = float(time_interval)
                print("-Checking time interval dependencies")
                self._time_interval_updated()
            if internal is False:
                print("Time interval updated by user")
                self._time_interval = time_interval

    def get_time_interval(self):
        if self._time_interval_:
            return self._time_interval_
        else:
            return 0.0

    def is_set_time_interval(self):
        if self._time_interval:
            return True
        else:
            return False

    # time_steps
    def set_time_steps(self, time_steps, internal=False):
        if self._time_steps_ != time_steps:
            print("Time step changed")
            if time_steps:
                self._time_steps_ = float(time_steps)
                print("-Checking time step dependencies")
                self._time_step_updated()
            if internal is False:
                print("Time step updated by user")
                self._time_steps = time_steps

    def get_time_steps(self):
        if self._time_steps_:
            return self._time_steps_
        else:
            return 0.0

    def is_set_time_steps(self):
        if self._time_steps:
            return True
        else:
            return False

    # delta_x
    def set_delta_x(self, delta_x, internal=False):
        if self._delta_x_ != delta_x:
            print("Delta x changed")
            if delta_x:
                self._delta_x_ = float(delta_x)
                print("-Checking delta x dependencies")
                self._delta_x_updated()
            if internal is False:
                print("Delta x updated by user")
                self._delta_x = delta_x

    def get_delta_x(self):
        if self._delta_x_:
            return self._delta_x_
        else:
            return 0.0

    def is_set_delta_x(self):
        if self._delta_x:
            return True
        else:
            return False

    # reference_length
    def set_reference_length(self, reference_length, internal=False):
        if self._reference_length_ != reference_length:
            print("Reference length changed")
            if reference_length:
                self._reference_length_ = float(reference_length)
                print("-Checking reference length dependencies")
                self._reference_length_updated()
            if internal is False:
                print("Reference length updated by user")
                self._reference_length = reference_length

    def get_reference_length(self):
        if self._reference_length_:
            return self._reference_length_
        else:
            return 0.0

    def is_set_reference_length(self):
        if self._reference_length:
            return True
        else:
            return False

    # number_of_nodes
    def set_number_of_nodes(self, number_of_nodes, internal=False):
        if self._number_of_nodes_ != number_of_nodes:
            print("Number of nodes changed")
            if number_of_nodes:
                self._number_of_nodes_ = float(number_of_nodes)
                print("-Checking number of nodes dependencies")
                self._number_of_nodes_updated()
            if internal is False:
                print("Number of nodes updated by user")
                self._number_of_nodes = number_of_nodes

    def get_number_of_nodes(self):
        if self._number_of_nodes_:
            return self._number_of_nodes_
        else:
            return 0.0

    def is_set_number_of_nodes(self):
        if self._number_of_nodes:
            return True
        else:
            return False

    """Functions caled when value is updated to update all possible
    resulting value changes.
    """
    # velocity
    def _velocity_updated(self):
        # Maybe just make function that goes through all available 
        # variabels and trys to calculate each...
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
        # time_interval from velocity
        if self._velocity_ and not self._time_interval_:
            self.set_time_interval(self._calc_time_from_flow_distance_(), True)
        # velocity from time_interval
        elif self._time_interval_ and not self._velocity_:
            self.set_velocity(self._calc_velocity_from_distance(), True)

    # delta_t
    def _delta_t_updated(self):
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
        # delta_t from time_interval
        if self._time_interval_ and not self._delta_t_:
            self.set_delta_t(self._calc_delta_t_from_time_and_steps(), True)
        # time_interval from delta_t
        elif self._delta_t_ and not self._time_interval_:
            self.set_time_steps(self._calc_time_from_delta_t_(), True)

    # reference_length
    def _reference_length_updated(self):
        # delta_x from number_of_nodes
        if self._number_of_nodes_ and not self._delta_x_:
            self.set_delta_x(self._calc_delta_x_from_length(), True)
        # number_of_nodes from delta_x
        elif self._delta_x_ and not self._number_of_nodes_:
            self.set_number_of_nodes(self._calc_num_nodes_from_delta_x_(), True)

    # number_of_nodes
    def _number_of_nodes_updated(self):
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
    # Reset values
    def reset_values(self):
        print("Resetting values")
        self.set_velocity(None)
        self.set_flow_distance(None)
        self.set_delta_t(None)
        self.set_delta_x(None)
        self.set_time_interval(None)
        self.set_time_steps(None)
        self.set_reference_length(None)
        self.set_number_of_nodes(None)
        self.reset_internal_values()

    # Reset all internal values for recalculation
    def reset_internal_values(self):
        # Reset all values
        print("Resetting internal values")
        self._velocity_ = self._velocity
        self._flow_distance_ = self._flow_distance
        self._delta_t_ = self._delta_t
        self._time_interval_ = self._time_interval
        self._time_steps_ = self._time_steps
        self._delta_x_ = self._delta_x
        self._reference_length_ = self._reference_length
        self._number_of_nodes_ = self._number_of_nodes

        # Checks should be made here to recalculate resultants of
        # set values
        print("Recalculating internal values")
        if self._velocity:
            print("-Checking velocity dependencies")
            self._velocity_updated()
        if self._flow_distance:
            print("-Checking flow distance dependencies")
            self._flow_distance_update()
        if self._delta_t:
            print("-Checking delta t dependencies")
            self._delta_t_updated()
        if self._time_interval:
            print("-Checking time interval dependencies")
            self._time_interval_updated()
        if self._time_steps:
            print("-Checking time step dependencies")
            self._time_step_updated()
        if self._delta_x:
            print("-Checking delta x dependencies")
            self._delta_x_updated()
        if self._reference_length:
            print("-Checking reference length dependencies")
            self._reference_length_updated()
        if self._number_of_nodes:
            print("-Checking number of nodes dependencies")
            self._number_of_nodes_updated()
        # Consider adding flags that may be used by gui later
        print("Completed value updates")