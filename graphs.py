#Created by Ali Adnan & Peter Ngo

#Start-------------

import matplotlib.pyplot as plt

# Data from the lab results
masses = [61.45, 76.87, 82.09]  # Mass of Brass samples in grams
temperatures = [21.5, 22.0, 23.0]  # Resulting water temperatures in degrees Celsius
initial_water_temp = 19  # Initial water temperature in degrees Celsius
specific_heat_water = 4.18  # Specific heat of water in J/g°C
water_mass = 140  # Volume of water in ml, assuming 1g/ml density for water

# Calculate heat capacity for each sample (q = m * c * ΔT)
heat_capacities = [
    water_mass * specific_heat_water * (temp - initial_water_temp) for temp in temperatures
]

# Plot 1: Mass of Brass vs Temperature
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(masses, temperatures, marker='o', color='b', label="Temperature")
plt.title("Mass of Brass vs Water Temperature")
plt.xlabel("Mass of Brass (g)")
plt.ylabel("Water Temperature (°C)")
plt.grid(True)
plt.legend()

# Plot 2: Mass of Brass vs Heat Capacity
plt.subplot(1, 2, 2)
plt.plot(masses, heat_capacities, marker='o', color='r', label="Heat Capacity")
plt.title("Mass of Brass vs Heat Capacity of the System")
plt.xlabel("Mass of Brass (g)")
plt.ylabel("Heat Capacity (J)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

#End----------------
