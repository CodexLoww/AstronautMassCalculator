import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Stage 2: Astronaut Mass Calculator")

# Define the celestial body mass multipliers
celestial_bodies = {
    'Moon': 0.166,
    'Mercury': 0.378,
    'Venus': 0.907,
    'Mars': 0.377,
    'Lo': 0.1835,
    'Europa': 0.1335,
    'Ganymede': 0.1448,
    'Callisto': 0.1264
}

# Define function to calculate the weight of personal items
def calculate_weight():
    # Clear any previous error messages
    error_label.config(text="")

    # Get the mass allowance for flight crew
    flight_crew_allowances = []
    for i in range(3):
        allowance = flight_crew_entries[i].get()
        if allowance == "":
            allowance = 0
        # Validate input - only accept numeric values
        if not allowance.isnumeric():
            error_label.config(text="Mass allowance for Flight Crew must be a numeric value.")
        allowance = float(allowance)
        if allowance > 100:
            error_label.config(text="Error: Mass allowance for Flight Crew cannot exceed 100 kg.")
            return
        else:
            flight_crew_allowances.append(allowance)

    # Get the mass allowance for mission specialist
    mission_specialist_allowances = []
    for i in range(3):
        allowance = mission_specialist_entries[i].get()
        if allowance == "":
            allowance = 0
        # Validate input - only accept numeric values
        if not allowance.isnumeric():
            error_label.config(text="Mass allowance for Mission Specialist must be a numeric value.")
        allowance = float(allowance)
        if allowance > 150:
            error_label.config(text="Error: Mass allowance for Mission Specialist cannot exceed 150 kg.")
            return
        else:
            mission_specialist_allowances.append(allowance)

    # Calculate the total available mass for personal items
    total_available_mass = sum(flight_crew_allowances) + sum(mission_specialist_allowances)

    # Calculate the average available personal mass allowance across all six astronauts
    avg_available_mass = total_available_mass / 6

    # Get the destination celestial body and its mass multiplier
    destination = destination_var.get()
    if destination not in celestial_bodies:
        error_label.config(text="Error: Invalid destination.")
        return
    mass_multiplier = celestial_bodies[destination]

    # Display the mass multiplier for the destination
    multiplier_label.config(text="Mass multiplier for {} is {}".format(destination, mass_multiplier))

    # Calculate the weight of the average available personal mass allowance on the celestial body
    weight_avg_mass = avg_available_mass * mass_multiplier

    # Calculate how much mass each astronaut has left over for personal items
    flight_crew_mass_left = [allowance - (allowance * mass_multiplier) for allowance in flight_crew_allowances]
    mission_specialist_mass_left = [allowance - (allowance * mass_multiplier) for allowance in mission_specialist_allowances]

    # Update the result labels if you to rounded it up use "{:.2}"
    total_available_label.config(text="Total Available Mass: {} kg".format(total_available_mass))
    avg_available_label.config(text="Average available weight: {} kg".format(avg_available_mass))
    equiv_avg_label.config(text="Equivalent average on {}: {} kg\n".format(destination, weight_avg_mass))

    for i in range(3):
        flight_crew_labels[i].config(text="Flight Crew {}: {} kg".format(i+1, flight_crew_mass_left[i]))

    for i in range(3):    
        mission_specialist_labels[i].config(text="Mission Specialist {}: {} kg".format(i+1, mission_specialist_mass_left[i]))

# Create the input frame for the flight crew mass allowances
flight_crew_frame = tk.Frame(root)
flight_crew_frame.pack(padx=10, pady=10)

flight_crew_label = tk.Label(flight_crew_frame, text="Flight Crew Mass Allowance (kg)")

#Create the input fields for the flight crew mass allowances
flight_crew_entries = []
for i in range(3):
    label = tk.Label(flight_crew_frame, text="Flight Crew {}: ".format(i+1))
    label.grid(row=i, column=0, sticky="w")
    entry = tk.Entry(flight_crew_frame, width=10)
    entry.grid(row=i, column=1)
    flight_crew_entries.append(entry)

#Create the input frame for the mission specialist mass allowances
mission_specialist_frame = tk.Frame(root)
mission_specialist_frame.pack(padx=10, pady=10)

mission_specialist_label = tk.Label(mission_specialist_frame, text="Mission Specialist Mass Allowance (kg)")

#Create the input fields for the mission specialist mass allowances
mission_specialist_entries = []
for i in range(3):
    label = tk.Label(mission_specialist_frame, text="Mission Specialist {}: ".format(i+1))
    label.grid(row=i, column=0, sticky="w")
    entry = tk.Entry(mission_specialist_frame, width=10)
    entry.grid(row=i, column=1)
    mission_specialist_entries.append(entry)

#Create the input frame for the destination selection
destination_frame = tk.Frame(root)
destination_frame.pack(padx=10, pady=10)

destination_label = tk.Label(destination_frame, text="Select Destination:")
destination_label.pack(side="left")

destination_var = tk.StringVar(root)
destination_dropdown = tk.OptionMenu(destination_frame, destination_var, *celestial_bodies.keys())
destination_dropdown.pack(side="left")

#Create the button to calculate the weight of personal items
calculate_button = tk.Button(root, text="Calculate", command=calculate_weight)
calculate_button.pack(pady=10)

# Create the exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(side=tk.BOTTOM, padx=10, pady=10)

#Create the error label for displaying error messages
error_label = tk.Label(root, fg="red")
error_label.pack()

#Create the output frame for displaying results
output_frame = tk.Frame(root)
output_frame.pack(padx=10, pady=10)

multiplier_label = tk.Label(output_frame, text="Mass multiplier for is ")
multiplier_label.pack()

total_available_label = tk.Label(output_frame, text="Total Available Mass: ")
total_available_label.pack()

avg_available_label = tk.Label(output_frame, text="Average available weight is: ")
avg_available_label.pack()

equiv_avg_label = tk.Label(output_frame, text="Equivalent average on : \n")
equiv_avg_label.pack()

left_label = tk.Label(output_frame, text="Left Available Mass")
left_label.pack()

flight_crew_labels = []
mission_specialist_labels = []
for i in range(3):
    flight_crew_label = tk.Label(output_frame, text="Flight Crew {}: ".format(i+1))
    flight_crew_label.pack()
    flight_crew_labels.append(flight_crew_label)

for i in range(3):    
    mission_specialist_label = tk.Label(output_frame, text="Mission Specialist {}: ".format(i+1))
    mission_specialist_label.pack()
    mission_specialist_labels.append(mission_specialist_label)

root.mainloop()