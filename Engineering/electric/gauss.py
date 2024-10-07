import numpy as np
import matplotlib.pyplot as plt

# Constants
epsilon_0 = 8.854187817e-12  # Vacuum permittivity in F/m

# Create a grid of points
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Assume a uniform electric field (E_x, E_y) for simplicity
E_x = np.ones_like(X)
E_y = np.zeros_like(Y)

# Calculate divergence of the electric field
div_E = np.gradient(E_x, x[1] - x[0], axis=0) + np.gradient(E_y, y[1] - y[0], axis=1)

# Plotting
plt.figure(figsize=(10, 6))
plt.contourf(X, Y, div_E, levels=np.linspace(-1, 1, 100), cmap='RdBu', vmin=-1, vmax=1)
plt.colorbar(label='Divergence of Electric Field')
plt.title('Divergence of Electric Field in a Charge-Free Region')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()