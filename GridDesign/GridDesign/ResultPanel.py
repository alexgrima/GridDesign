import wx

class ResultPanel(wx.Panel):
    """Panel contating all output variabels.
    """
    # Initialise the panel
    def __init__(self, parent, ID):
        """Intialise all user input fields and set to 0.0.
        """        
        wx.Panel.__init__(self, parent, -1)

        # Add labels and vvalue areas
        # velcoity or rotor tip speed
        self.velocity_box = wx.BoxSizer(wx.HORIZONTAL)
        self.velocity_label = wx.StaticText(self, -1, "Velocity:")
        self.velocity_value = wx.TextCtrl(self, -1, "0.00", style=wx.TE_READONLY)
        self.velocity_box.Add(self.velocity_label, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        self.velocity_box.Add(self.velocity_value, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)

        # Time interval
        self.ti_box = wx.BoxSizer(wx.HORIZONTAL)
        self.ti_label = wx.StaticText(self, -1, "Time interval:")
        self.ti_value = wx.TextCtrl(self, -1, "0.00", style=wx.TE_READONLY)
        self.ti_box.Add(self.ti_label, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        self.ti_box.Add(self.ti_value, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)

        # Time steps
        self.ts_box = wx.BoxSizer(wx.HORIZONTAL)
        self.ts_label = wx.StaticText(self, -1, "Time steps:")
        self.ts_value = wx.TextCtrl(self, -1, "0.00", style=wx.TE_READONLY)
        self.ts_box.Add(self.ts_label, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        self.ts_box.Add(self.ts_value, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)

        # Reference length
        self.rl_box = wx.BoxSizer(wx.HORIZONTAL)
        self.rl_label = wx.StaticText(self, -1, "Reference length:")
        self.rl_value = wx.TextCtrl(self, -1, "0.00", style=wx.TE_READONLY)
        self.rl_box.Add(self.rl_label, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        self.rl_box.Add(self.rl_value, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)

        # Number of nodes
        self.nn_box = wx.BoxSizer(wx.HORIZONTAL)
        self.nn_label = wx.StaticText(self, -1, "Number of nodes:")
        self.nn_value = wx.TextCtrl(self, -1, "0.00", style=wx.TE_READONLY)
        self.nn_box.Add(self.nn_label, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        self.nn_box.Add(self.nn_value, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)

        # Add to main sizer
        self.main_box = wx.StaticBoxSizer(wx.StaticBox(self, -1, "Resultants"), wx.VERTICAL)
        self.main_box.Add(self.velocity_box, flag=wx.ALIGN_RIGHT)
        self.main_box.Add(self.ti_box, flag=wx.ALIGN_RIGHT)
        self.main_box.Add(self.ts_box, flag=wx.ALIGN_RIGHT)
        self.main_box.Add(self.rl_box, flag=wx.ALIGN_RIGHT)
        self.main_box.Add(self.nn_box, flag=wx.ALIGN_RIGHT)

        # Finalise size
        self.SetSizer(self.main_box)
        self.Layout()

    # Update all values from freestream
    def freestream_value_update(self, freestream):
        self.velocity_value.SetValue(str(freestream.get_velocity()))
        self.ti_value.SetValue(str(freestream.get_time_interval()))
        self.ts_value.SetValue(str(freestream.get_time_steps()))
        self.rl_value.SetValue(str(freestream.get_reference_length()))
        self.nn_value.SetValue(str(freestream.get_number_of_nodes()))