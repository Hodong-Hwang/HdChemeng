import matplotlib.pyplot as plt
import numpy as np
import glob
import imageio.v2 as imageio

def read_data(filename):
    data = np.loadtxt(filename)
    return data[:, 0], data[:, 1], data[:, 2]

filenames = sorted(glob.glob("output_*.dat"))
images = []

for filename in filenames:
    rho, u, p = read_data(filename)
    plt.figure()
    plt.plot(rho, label='Density')
    plt.plot(u, label='Velocity')
    plt.plot(p, label='Pressure')
    plt.legend()
    plt.title(f"Time step {filename.split('_')[1].split('.')[0]}")
    plt.xlabel('Spatial Index')
    plt.ylabel('Values')
    
    plt.savefig("temp.png")
    plt.close()
    
    images.append(imageio.imread("temp.png"))

imageio.mimsave("output.gif", images, duration=0.1)