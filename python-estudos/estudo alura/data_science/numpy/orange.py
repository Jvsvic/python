import numpy as np

url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv'
dado = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 6, 1), skiprows=1)



dado_transposto = dado.T
print(dado_transposto)
print(dado.shape)
print(dado.size)
print(dado.ndim)