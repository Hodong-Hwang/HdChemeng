import numpy as np

# Define two vectors
u = np.array([1, 2, 3])
v = np.array([4, 5])

# Compute the outer product
outer_product = np.outer(u, v)

print("Vector u:", u)
print("Vector v:", v)
print("Outer Product:\n", outer_product)