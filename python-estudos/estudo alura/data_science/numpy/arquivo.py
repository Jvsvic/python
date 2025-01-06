
import numpy as np

url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'
data = np.loadtxt('apples_ts.csv', delimiter=',', skiprows=1)
dado = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 88, 1))


#print(dado.ndim)
#print(dado.size)
#print(dado.shape)


dado_transposto = dado.T
print(dado_transposto)
print(dado.shape)
print(dado.size)
print(dado.ndim)