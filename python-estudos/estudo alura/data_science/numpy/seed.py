import numpy as np

np.random.seed(42)
a = np.random.uniform(0, 5, 5)
np.random.seed(8)
b = np.random.uniform(0, 5, 5)
print(a)
print(b)