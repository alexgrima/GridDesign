import wx

class ControlPanel(wx.Panel):
    """Panel containing the radio buttons used for choosing what to
    dimension for.
    """
    # Initialise the panel
    def __init__(self, parent, ID):
        """Intialise each radio button.
        """        
        wx.Panel.__init__(self, parent, -1)
        
        # Add radio buttons
        self.freestream_radio = wx.RadioButton(parent, -1, 
                                "Freestream")
        self.rotor_radio = wx.RadioButton(parent, -1,
                                            "Rotor")

        # Add sizer
        self.radio_box = wx.StaticBoxSizer(wx.StaticBox(self, 
                         -1, "Choose dimensioning type"), 
                         wx.HORIZONTAL)
        self.radio_box.Add(self.freestream_radio, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        self.radio_box.Add(self.rotor_radio, border=5, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)

        # Finalise size
        self.SetSizer(self.radio_box)
        self.Layout()
