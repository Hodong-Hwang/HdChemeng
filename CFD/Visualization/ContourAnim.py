import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Set parameters
nx = 50  # Number of grid points in x-direction
ny = 50  # Number of grid points in y-direction
nt = 100  # Number of time steps
dt = 0.01  # Time step size
nu = 0.1  # Kinematic viscosity

# Set grid spacing
dx = 2 / (nx - 1)
dy = 2 / (ny - 1)

# Initialize velocity and pressure fields
u = np.zeros((nx, ny))
v = np.zeros((nx, ny))
p = np.zeros((nx, ny))
b = np.zeros((nx, ny))  # Divergence term
pn = np.zeros((nx, ny))  # Pressure field at previous time step

# Set up the figure and axis
fig, ax = plt.subplots()
x = np.linspace(0.0, 1, nx)
y = np.linspace(0.0, 1, ny)
X, Y = np.meshgrid(x, y)
# Create an empty contour plot for the pressure field
pressure_plot = ax.contourf(X, Y, p)

# Function to update the plot for each animation frame
def update_plot(frame):
    # Perform the calculations for the next time step
    # ...
    
    # Update the pressure plot
    pressure_plot = ax.contourf(p, levels=20)

    # Return the updated plot objects
    return [pressure_plot]

# Create the animation
anim = animation.FuncAnimation(fig, update_plot, frames=nt, blit=False)

# Set up the writer for saving the animation as a GIF file
Writer = animation.writers['pillow']
writer = Writer(fps=15)

# Save the animation
anim.save('pressure_animation.gif', writer=writer)