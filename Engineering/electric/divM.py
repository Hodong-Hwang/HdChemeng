import numpy as np
import matplotlib.pyplot as plt

# Constants
size = 2.0  # Size of the grid

# Create a grid of points
x = np.linspace(-size, size, 100)
y = np.linspace(-size, size, 100)
X, Y = np.meshgrid(x, y)

# Electric field components (example with uniform electric field)
E_x = np.ones_like(X)  # Uniform field in x-direction
E_y = np.zeros_like(Y)  # No y-component

# Magnetic field components (example with uniform magnetic field)
B_x = np.zeros_like(X)  # No x-component
B_y = np.ones_like(Y)  # Uniform field in y-direction

# Calculate divergence of the electric field
div_E = np.gradient(E_x, x[1] - x[0], axis=0) + np.gradient(E_y, y[1] - y[0], axis=1)

# Calculate divergence of the magnetic field
div_B = np.gradient(B_x, x[1] - x[0], axis=0) + np.gradient(B_y, y[1] - y[0], axis=1)

# Plotting Electric Field Divergence
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.contourf(X, Y, div_E, levels=np.linspace(-1, 1, 100))
plt.colorbar(label='Divergence of Electric Field')
plt.title('Divergence of Electric Field (E)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# Plotting Magnetic Field Divergence
plt.subplot(1, 2, 2)
plt.contourf(X, Y, div_B, levels=np.linspace(-1, 1, 100))
plt.colorbar(label='Divergence of Magnetic Field')
plt.title('Divergence of Magnetic Field (B)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

plt.tight_layout()
plt.show()