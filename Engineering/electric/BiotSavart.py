import numpy as np
import matplotlib.pyplot as plt

# Constants
mu_0 = 4 * np.pi * 1e-7  # Vacuum permeability
I = 1.0  # Current in amperes

# Create a grid of points
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Calculate the distance from the current-carrying wire (assumed along the x-axis)
R = np.sqrt(X**2 + Y**2)
R[R == 0] = np.nan  # Avoid division by zero

# Calculate magnetic field components using Biot-Savart Law
B = (mu_0 * I) / (2 * np.pi * R)

# Convert Cartesian coordinates to polar for plotting
theta = np.arctan2(Y, X)
Bx = -B * np.sin(theta)
By = B * np.cos(theta)

# Plotting
plt.figure(figsize=(8, 8))
plt.streamplot(X, Y, Bx, By, color='b', linewidth=1, density=1.5)
plt.title('Magnetic Field around a Long Straight Current-Carrying Wire')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='k', linewidth=0.5)
plt.axvline(0, color='k', linewidth=0.5)
plt.show()