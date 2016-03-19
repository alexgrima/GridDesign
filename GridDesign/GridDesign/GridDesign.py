from Freestream import Freestream

# Function that sets the value to the variabel specified
def set_variabel(freestream, variable, value):
    if str(variable).lower() == "":
        pass
    elif str(variable).lower() in "v":
        freestream.set_velocity(float(value))
    elif str(variable).lower() in "fd":
        freestream.set_flow_distance(float(value))
    elif str(variable).lower() in "dt":
        freestream.set_delta_t(float(value))
    elif str(variable).lower() in "dx":
        freestream.set_delta_x(float(value))
    elif str(variable).lower() in "ti":
        freestream.set_time_interval(float(value))
    elif str(variable).lower() in "ts":
        freestream.set_time_step(float(value))
    elif str(variable).lower() in "rl":
        freestream.set_reference_length(float(value))
    elif str(variable).lower() in "nn":
        freestream.set_number_of_nodes(float(value))


# main function
def main():
    # Generate instance of freestream calculator
    freestream_calc = Freestream()

    # Inifinate loop
    while True:
        print("\n" +str(freestream_calc))
        print("What variable would you like to change?")
        print("V, FD, dt, dx, ti, ts, rl, nn")
        choise = raw_input("Choise: ")
        value = raw_input("Value: ")
        set_variabel(freestream_calc, choise, value)

main()