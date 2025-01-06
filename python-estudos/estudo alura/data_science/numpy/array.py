import numpy as np

url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/bytebank.csv'
dado = np.loadtxt(url, delimiter=',', skiprows=1, dtype=float)
print(dado.ndim)
print(dado.size)
print(dado.shape)
print(np.shape(dado))