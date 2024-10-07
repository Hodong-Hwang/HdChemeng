import numpy as np
import matplotlib.pyplot as plt

# Constants
mu_0 = 4 * np.pi * 1e-7  # Vacuum permeability in T*m/A
I = 1.0  # Current in amperes
r_max = 2.0  # Maximum radius to consider in meters
num_points = 100  # Number of points in the plot

# Create a grid of points
r = np.linspace(0.01, r_max, num_points)  # Avoid division by zero by starting at 0.01
B = (mu_0 * I) / (2 * np.pi * r)  # Magnetic field strength calculation

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(r, B, label='Magnetic Field B(r)')
plt.title('Magnetic Field Around a Long Straight Current-Carrying Wire')
plt.xlabel('Distance from the Wire (m)')
plt.ylabel('Magnetic Field (T)')
plt.grid(True)
plt.legend()
plt.show()