
import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'
dado = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 88, 1))


#print(dado.ndim)
#print(dado.size)
#print(dado.shape)


dado_transposto = dado.T
#datas = dado_transposto[0:2]
precos = dado_transposto[:,1:6]
datas = np.arange(1,88,1)
#plt.plot(datas, precos[:,0])
#plt.show()

Moscow = precos[:,0]
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]
#print(Moscow)
#print(Moscow.shape)
Moscow_ano1 = Moscow[0:12] 
Moscow_ano2 = Moscow[12:24]
Moscow_ano3 = Moscow[24:36]
Moscow_ano4 = Moscow[36:48]
#print(Moscow_ano1) 
#plt.plot(np.arange(1,13,1), Moscow_ano1)
#plt.plot(np.arange(1,13,1), Moscow_ano2)
#plt.plot(np.arange(1,13,1), Moscow_ano3)
#plt.plot(np.arange(1,13,1), Moscow_ano4)
#print(np.array_equal(Moscow_ano1,Moscow_ano4))
#print(np.allclose(Moscow_ano3, Moscow_ano4,10))


#print(sum(np.isnan(Kaliningrad)))
#plt.legend(['ano1', 'ano2', 'ano3', 'ano4'])
Kaliningrad[4] = (np.mean([Kaliningrad[3],Kaliningrad[5]]))
#print(Kaliningrad[4])


#print(np.mean(Moscow))
#print(np.mean(Kaliningrad))


#x = datas
#y = 2*x+80
#y = 0.52 * x + 80
#plt.plot(datas, Moscow)
#plt.show(x,y)

#plt.plot(x,y)
#plt.show()
#print(np.sqrt(np.sum(np.power(Moscow-y,2))))
#print(np.linalg.norm(Moscow-y))
Y = Moscow
X = datas
n = np.size(Moscow)
#print((X**2).shape)
a = (n*np.sum(X*Y) - np.sum(X)*np.sum(Y))/(n*np.sum(X**2) - np.sum(X)**2)
#print(a)
b = np.mean(Y) - a*np.mean(X)
#print(b)
y = a*X+b
#print(np.linalg.norm(Moscow-y))
plt.plot(datas,Moscow)
plt.plot(X,y)
plt.plot(41.5,41.5*a+b,'*r')
plt.plot(100,100*a+b,'*r')
#plt.show()

int = np.random.randint(low=40, high=100, size=100)
coef = np.random.uniform(low=0.10, high=0.90, size=100)
norma2 = np.array([])
for i in range(100):
    norma2 = np.append(norma2, np.linalg.norm(Moscow-(coef[i]*X+b)))

#print(np.random.seed(84))
np.random.uniform(low=0.10, high=0.90, size=100)
#print(coef)

dados = np.column_stack([norma2, coef])
print(dados.shape)
np.savetxt('dados.csv', dados, delimiter=',' )