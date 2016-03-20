import wx

class FreestreamPanel(wx.Panel):
    """Panel containing all input fields for the freemstream sizing.
    """
    # Initialise the panel
    def __init__(self, parent, ID):
        """Intialise all user input fields and set to 0.0.
        """        
        wx.Panel.__init__(self, parent, -1)

        # Add labels and spinners
        # velcoity
        self.velocity_box = wx.BoxSizer(wx.HORIZONTAL)
        self.velocity_label = wx.StaticText(self, -1, "Velocity:")
        self.velocity_spinner = wx.SpinCtrlDouble(self, value='0.00',
                                          min=0.00, max=9999)
        self.velocity_spinner.SetDigits(2)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.on_velocity_change, self.velocity_spinner)
        self.velocity_box.Add(self.velocity_label, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        self.velocity_box.Add(self.velocity_spinner, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)

        # flow distance
        self.flow_box = wx.BoxSizer(wx.HORIZONTAL)
        self.flow_label = wx.StaticText(self, -1, "Flow distance:")
        self.flow_spinner = wx.SpinCtrlDouble(self, value='0.00',
                                          min=0.00, max=9999)
        self.flow_spinner.SetDigits(2)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.on_distance_change, self.flow_spinner)
        self.flow_box.Add(self.flow_label, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        self.flow_box.Add(self.flow_spinner, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        
        # delta t
        self.deltat_box = wx.BoxSizer(wx.HORIZONTAL)
        self.deltat_label = wx.StaticText(self, -1, u"\u0394" +"t:")
        self.deltat_spinner = wx.SpinCtrlDouble(self, value='0.00',
                                          min=0.00, max=9999)
        self.deltat_spinner.SetDigits(2)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.on_deltat_change, self.deltat_spinner)
        self.deltat_box.Add(self.deltat_label, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        self.deltat_box.Add(self.deltat_spinner, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        
        # time interval
        self.ti_box = wx.BoxSizer(wx.HORIZONTAL)
        self.ti_label = wx.StaticText(self, -1, "Time interval:")
        self.ti_spinner = wx.SpinCtrlDouble(self, value='0.00',
                                          min=0.00, max=9999)
        self.ti_spinner.SetDigits(2)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.on_ti_change, self.ti_spinner)
        self.ti_box.Add(self.ti_label, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        self.ti_box.Add(self.ti_spinner, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        
        # time steps
        self.ts_box = wx.BoxSizer(wx.HORIZONTAL)
        self.ts_label = wx.StaticText(self, -1, "Time steps:")
        self.ts_spinner = wx.SpinCtrlDouble(self, value='0.00',
                                          min=0.00, max=9999)
        self.ts_spinner.SetDigits(2)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.on_ts_change, self.ts_spinner)
        self.ts_box.Add(self.ts_label, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        self.ts_box.Add(self.ts_spinner, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        
        # delta x
        self.deltax_box = wx.BoxSizer(wx.HORIZONTAL)
        self.deltax_label = wx.StaticText(self, -1, u"\u0394" +"x:")
        self.deltax_spinner = wx.SpinCtrlDouble(self, value='0.00',
                                          min=0.00, max=9999)
        self.deltax_spinner.SetDigits(2)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.on_deltax_change, self.deltax_spinner)
        self.deltax_box.Add(self.deltax_label, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        self.deltax_box.Add(self.deltax_spinner, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        
        # reference length
        self.rl_box = wx.BoxSizer(wx.HORIZONTAL)
        self.rl_label = wx.StaticText(self, -1, "Reference length:")
        self.rl_spinner = wx.SpinCtrlDouble(self, value='0.00',
                                          min=0.00, max=9999)
        self.rl_spinner.SetDigits(2)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.on_rl_change, self.rl_spinner)
        self.rl_box.Add(self.rl_label, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        self.rl_box.Add(self.rl_spinner, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        
        # number of nodes
        self.nn_box = wx.BoxSizer(wx.HORIZONTAL)
        self.nn_label = wx.StaticText(self, -1, "Number of nodes:")
        self.nn_spinner = wx.SpinCtrlDouble(self, value='0.00',
                                          min=0.00, max=9999)
        self.nn_spinner.SetDigits(2)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.on_nn_change, self.nn_spinner)
        self.nn_box.Add(self.nn_label, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        self.nn_box.Add(self.nn_spinner, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)

        # reset
        self.reset_button = wx.Button(self, -1, "Reset")
        self.Bind(wx.EVT_BUTTON, self.on_reset, self.reset_button)
        
        # Add to main sizer
        self.main_box = wx.StaticBoxSizer(wx.StaticBox(self, -1, "Freestream values"), wx.VERTICAL)
        self.main_box.Add(self.velocity_box, flag=wx.ALIGN_RIGHT)
        self.main_box.Add(self.flow_box, flag=wx.ALIGN_RIGHT)
        self.main_box.Add(self.deltat_box, flag=wx.ALIGN_RIGHT)
        self.main_box.Add(self.ti_box, flag=wx.ALIGN_RIGHT)
        self.main_box.Add(self.ts_box, flag=wx.ALIGN_RIGHT)
        self.main_box.Add(self.deltax_box, flag=wx.ALIGN_RIGHT)
        self.main_box.Add(self.rl_box, flag=wx.ALIGN_RIGHT)
        self.main_box.Add(self.nn_box, flag=wx.ALIGN_RIGHT)
        self.main_box.Add(self.reset_button, border = 5, flag=wx.ALIGN_CENTER)

        # Finalise size
        self.SetSizer(self.main_box)
        self.Layout()

    # Functions to update values
    def on_velocity_change(self, event):
        if event.GetValue() == 0.0:
            self.Parent.Parent.freestream.set_velocity(None)
            self.velocity_spinner.SetValue(0.00)
            self.Parent.Parent.freestream_values_updated()
        elif event.GetValue() != self.Parent.Parent.freestream.get_velocity():
            self.Parent.Parent.freestream.set_velocity(event.GetValue())
            self.Parent.Parent.freestream_values_updated()

    def on_distance_change(self, event):
        if event.GetValue() == 0.0:
            self.Parent.Parent.freestream.set_flow_distance(None)
            self.flow_spinner.SetValue(0.00)
            self.Parent.Parent.freestream_values_updated()
        elif event.GetValue() != self.Parent.Parent.freestream.get_flow_distance():
            self.Parent.Parent.freestream.set_flow_distance(event.GetValue())
            self.Parent.Parent.freestream_values_updated()

    def on_deltat_change(self, event):
        if event.GetValue() == 0.0:
            self.Parent.Parent.freestream.set_delta_t(None)
            self.deltat_spinner.SetValue(0.00)
            self.Parent.Parent.freestream_values_updated()
        elif event.GetValue() != self.Parent.Parent.freestream.get_delta_t():
            self.Parent.Parent.freestream.set_delta_t(event.GetValue())
            self.Parent.Parent.freestream_values_updated()

    def on_ti_change(self, event):
        if event.GetValue() == 0.0:
            self.Parent.Parent.freestream.set_time_interval(None)
            self.ti_spinner.SetValue(0.00)
            self.Parent.Parent.freestream_values_updated()
        elif event.GetValue() != self.Parent.Parent.freestream.get_time_interval():
            self.Parent.Parent.freestream.set_time_interval(event.GetValue())
            self.Parent.Parent.freestream_values_updated()

    def on_ts_change(self, event):
        if event.GetValue() == 0.0:
            self.Parent.Parent.freestream.set_time_steps(None)
            self.ts_spinner.SetValue(0.00)
            self.Parent.Parent.freestream_values_updated()
        elif event.GetValue() != self.Parent.Parent.freestream.get_time_steps():
            self.Parent.Parent.freestream.set_time_steps(event.GetValue())
            self.Parent.Parent.freestream_values_updated()

    def on_deltax_change(self, event):
        if event.GetValue() == 0.0:
            self.Parent.Parent.freestream.set_delta_x(None)
            self.deltax_spinner.SetValue(0.00)
            self.Parent.Parent.freestream_values_updated()
        elif event.GetValue() != self.Parent.Parent.freestream.get_delta_x():
            self.Parent.Parent.freestream.set_delta_x(event.GetValue())
            self.Parent.Parent.freestream_values_updated()

    def on_rl_change(self, event):
        if event.GetValue() == 0.0:
            self.Parent.Parent.freestream.set_reference_length(None)
            self.rl_spinner.SetValue(0.00)
            self.Parent.Parent.freestream_values_updated()
        elif event.GetValue() != self.Parent.Parent.freestream.get_reference_length():
            self.Parent.Parent.freestream.set_reference_length(event.GetValue())
            self.Parent.Parent.freestream_values_updated()

    def on_nn_change(self, event):
        if event.GetValue() == 0.0:
            self.Parent.Parent.freestream.set_number_of_nodes(None)
            self.nn_spinner.SetValue(0.00)
            self.Parent.Parent.freestream_values_updated()
        elif event.GetValue() != self.Parent.Parent.freestream.get_number_of_nodes():
            self.Parent.Parent.freestream.set_number_of_nodes(event.GetValue())
            self.Parent.Parent.freestream_values_updated()

    def on_reset(self, event):
        self.Parent.Parent.freestream.reset_values()
        self.reset_values()
        self.Parent.Parent.freestream_values_updated()

    def reset_values(self):
        self.velocity_spinner.SetValue(0.00)
        self.flow_spinner.SetValue(0.00)
        self.deltat_spinner.SetValue(0.00)
        self.ti_spinner.SetValue(0.00)
        self.ts_spinner.SetValue(0.00)
        self.deltax_spinner.SetValue(0.00)
        self.rl_spinner.SetValue(0.00)
        self.nn_spinner.SetValue(0.00)