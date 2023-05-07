# Define the celestial body mass multipliers
celestial_bodies = {
    'Moon': 0.166,
    'Mercury': 0.378,
    'Venus': 0.907,
    'Mars': 0.377,
    'Io': 0.1835,
    'Europa': 0.1335,
    'Ganymede': 0.1448,
    'Callisto': 0.1264
}

# Get the mass allowance for flight crew
flight_crew_allowances = []
for i in range(3):
    while True:
        allowance = float(input(f"Enter mass allowance for Flight Crew {i+1} (in kg): "))
        if allowance > 100:
            print("Error: Mass allowance for Flight Crew cannot exceed 100 kg.")
        else:
            flight_crew_allowances.append(allowance)
            break

# Get the mass allowance for mission specialist
mission_specialist_allowances = []
for i in range(3):
    while True:
        allowance = float(input(f"Enter mass allowance for Mission Specialist {i+1} (in kg): "))
        if allowance > 150:
            print("Error: Mass allowance for Mission Specialist cannot exceed 150 kg.")
        else:
            mission_specialist_allowances.append(allowance)
            break

# Calculate the total available mass for personal items
total_available_mass = sum(flight_crew_allowances) + sum(mission_specialist_allowances)

# Calculate the average available personal mass allowance across all six astronauts
avg_available_mass = total_available_mass / 6

# Get the destination celestial body and its mass multiplier
destination = input("Enter the celestial body the astronauts are traveling to: ")
mass_multiplier = celestial_bodies[destination]

# Calculate the weight of the average available personal mass allowance on the celestial body
weight_avg_mass = avg_available_mass * mass_multiplier

# Calculate how much mass each astronaut has left over for personal items
flight_crew_mass_left = [allowance - (allowance * mass_multiplier) for allowance in flight_crew_allowances]
mission_specialist_mass_left = [allowance - (allowance * mass_multiplier) for allowance in mission_specialist_allowances]

# Display the results
print("Destination: ", destination)
print(f"Mass multiplier for {destination} is {mass_multiplier}")
for i, allowance in enumerate(flight_crew_mass_left):
    print(f"Flight Crew {i+1} personal mass allowance: {allowance} kg")
for i, allowance in enumerate(mission_specialist_mass_left):
    print(f"Mission Specialist {i+1} personal mass allowance: {allowance} kg")
print("Total available mass: ", total_available_mass, "kg")
print("Average available weights is: ", avg_available_mass, "kg")
print("Equivalent Average on Destination: ", weight_avg_mass, "kg")
