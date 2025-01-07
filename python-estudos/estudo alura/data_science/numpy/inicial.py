
import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'
dado = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 88, 1))


#print(dado.ndim)
#print(dado.size)
#print(dado.shape)


dado_transposto = dado.T
datas = dado_transposto[0:2]
precos = dado_transposto[:,1:6]
datas = np.arange(1,88,1)
#plt.plot(datas, precos[:,0])
#plt.show()

Moscow = precos[:,0]
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]
print(Moscow)
print(Moscow.shape)
Moscow_ano1 = Moscow[0:12] 
Moscow_ano2 = Moscow[12:24]
Moscow_ano3 = Moscow[24:36]
Moscow_ano4 = Moscow[36:48]
print(Moscow_ano1) 
plt.plot(np.arange(1,13,1), Moscow_ano1)
plt.plot(np.arange(1,13,1), Moscow_ano2)
plt.plot(np.arange(1,13,1), Moscow_ano3)
plt.plot(np.arange(1,13,1), Moscow_ano4)
#print(np.array_equal(Moscow_ano1,Moscow_ano4))
#print(np.allclose(Moscow_ano3, Moscow_ano4,10))


print(sum(np.isnan(Kaliningrad)))
#plt.legend(['ano1', 'ano2', 'ano3', 'ano4'])
Kaliningrad[4] = (np.mean([Kaliningrad[3],Kaliningrad[5]]))
print(Kaliningrad[4])
plt.plot(datas, Kaliningrad)
plt.show()
print(np.mean(Moscow))
print(np.mean(Kaliningrad))