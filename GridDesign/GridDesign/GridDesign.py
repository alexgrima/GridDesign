from Freestream import Freestream
from MainFrame import MainFrame
import wx

# Function that sets the value to the variabel specified
def set_variabel(freestream, variable, value):
    # If value empty set to None
    if str(value) == "":
        value = None
    # Set value
    if str(variable).lower() == "":
        pass
    elif str(variable).lower() in "v":
        freestream.set_velocity(value)
    elif str(variable).lower() in "fd":
        freestream.set_flow_distance(value)
    elif str(variable).lower() in "dt":
        freestream.set_delta_t(value)
    elif str(variable).lower() in "dx":
        freestream.set_delta_x(value)
    elif str(variable).lower() in "ti":
        freestream.set_time_interval(value)
    elif str(variable).lower() in "ts":
        freestream.set_time_step(value)
    elif str(variable).lower() in "rl":
        freestream.set_reference_length(value)
    elif str(variable).lower() in "nn":
        freestream.set_number_of_nodes(value)
    # Reset internal values of class before recomputing
    freestream.reset_internal_values()


# main function
def main():
    # Generate instance of freestream calculator
    freestream_calc = Freestream()

    # Create gui object
    app = wx.App(redirect=False)
    main_window = MainFrame(app, -1, "Grid design assitant", 
                            size=(350, 200), 
                            style = wx.DEFAULT_FRAME_STYLE)
    main_window.Show(True)
    app.MainLoop()

    # Inifinate loop
    while True:
        print("\n" +str(freestream_calc))
        print("What variable would you like to change?")
        print("V, FD, dt, dx, ti, ts, rl, nn")
        choise = raw_input("Choise: ")
        if str(choise).lower() == "reset":
            freestream_calc = Freestream()
        elif str(choise).lower() in ["quit", "exit"]:
            break
        else:
            value = raw_input("Value: ")
            print("")
            set_variabel(freestream_calc, choise, value)

main()