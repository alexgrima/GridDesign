from ControlPanel import ControlPanel
from FreestreamPanel import FreestreamPanel
from ResultPanel import ResultPanel
from Freestream import Freestream
import wx

class MainFrame(wx.Frame):
    """Main frame that contains the different input types and result
    column.
    """
    # Initialise
    def __init__(self, parent, ID, title, pos=wx.DefaultPosition,
            size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        """Create frame and add main panel to it for sizing.
        """
        wx.Frame.__init__(self, None, ID, title, pos, size, style)
        self.main_panel = wx.Panel(self, -1)

        # Value objects
        self.freestream = Freestream()

        # Add control panel
        self.control_panel = ControlPanel(self.main_panel, -1)

        # Add Freestream panel
        self.freestream_panel = FreestreamPanel(self.main_panel, -1)

        # Add Rotor panel

        # Add Result panel
        self.result_panel = ResultPanel(self.main_panel, -1)

        # Bind events
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        # Set sizers
        # Sizer for calculation panels
        self.value_box = wx.BoxSizer(wx.HORIZONTAL)
        self.value_box.Add(self.freestream_panel, border=5)
        self.value_box.Add(self.result_panel, border=5)
        # Main sizer
        self.main_box = wx.BoxSizer(wx.VERTICAL)
        self.main_box.Add(self.control_panel, border=5, flag=wx.ALIGN_CENTER_HORIZONTAL|wx.ALL)
        self.main_box.Add(self.value_box, border=5, flag=wx.ALIGN_CENTER_HORIZONTAL|wx.ALL)
        self.main_panel.SetSizer(self.main_box)
        self.main_panel.Layout()
        self.main_panel.Fit()
        self.Layout()
        self.Fit()

    # Function to destroy window upon closing it
    def OnCloseWindow(self, event):
        self.Destroy()

    # Values updated call to update resultant values
    def freestream_values_updated(self):
        # Reset internal values of class before recomputing
        self.freestream.reset_internal_values()
        self.result_panel.freestream_value_update(self.freestream)