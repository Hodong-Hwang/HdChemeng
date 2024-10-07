import numpy as np
import matplotlib.pyplot as plt

# Constants
N = 100  # Number of turns in the coil
A = 1.0  # Area of the coil in square meters
B_max = 1.0  # Maximum magnetic field strength in Tesla
T = 10  # Total time in seconds
dt = 0.01  # Time step in seconds
omega = 2 * np.pi / T  # Angular frequency

# Time array
time = np.arange(0, T, dt)

# Magnetic field strength as a function of time (sine wave)
B = B_max * np.sin(omega * time)

# Time derivative of the magnetic field
dB_dt = B_max * omega * np.cos(omega * time)

# Induced EMF calculation using Faraday's Law
emf = -N * A * dB_dt

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time, emf, label='Induced EMF (V)', color='b')
plt.title('Induced EMF in a Coil Due to Changing Magnetic Field')
plt.xlabel('Time (s)')
plt.ylabel('Induced EMF (V)')
plt.grid(True)
plt.legend()
plt.show()