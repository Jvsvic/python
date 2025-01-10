import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv'
dado = np.loadtxt(url, delimiter=',',usecols=np.arange(1,6,1),skiprows=1)
dado_transposto = dado.T
print(dado_transposto)
#Desafio de aula 
# -----------------

laranja = dado[:5000,0]
toranja = dado[5000:,0]
peso_laranja = dado[:5000,1]
peso_toranja = dado[5000:,1]


#FORMULA LARANJA
#------------------------------
y = peso_laranja
x = laranja
n = np.size(peso_laranja)
a = (n*np.sum(x*y) - np.sum(x)*np.sum(y))/(n*np.sum(x**2) - np.sum(x)**2)
b = np.mean(y) - a*np.mean(x)

y_laranja = a * x + b
print(np.linalg.norm(laranja-y))


#FORMULA TORANJA
#------------------------------------
y_toranja = peso_toranja
x_toranja = toranja
n_toranja = np.size(peso_toranja)
a_toranja = (n_toranja*np.sum(x_toranja*y_toranja) - np.sum(x_toranja)*np.sum(y_toranja))/(n_toranja*np.sum(x_toranja**2) - 
np.sum(x_toranja)**2)
print(np.linalg.norm(toranja-y_toranja))

b_toranja = np.mean(y_toranja) - a_toranja*np.mean(x_toranja)
ytoranja = a_toranja * x_toranja + b_toranja


#PLOTAGEM
#------------------------------------
#plt.plot(laranja, peso_laranja, color='red', label='Laranja')
plt.plot(toranja, peso_toranja, color='black', label='Toranja')
plt.plot(toranja,ytoranja, linestyle='dashed', color='yellow', label='linha_toranja')
#plt.plot(laranja, y_laranja, linestyle= 'dashed', color='yellow', label='linha')
plt.legend()
plt.show()

## -----------ULTIMA AULA

np.random.seed(1)
bc = 17
norma_laranja = np.array([])
norma_toranja = np.array([])
coef = np.random.uniform(low=0, high=30, size=100)
for i in range(100):
    norma_laranja = np.append(norma_laranja, np.linalg.norm(y_laranja - (coef[i]*x + bc)))
    norma_toranja = np.append(norma_toranja, np.linalg.norm(y_toranja - (coef[i]*x_toranja + bc)))

minimo_laranja = np.argmin(norma_laranja)
minimo_toranja = np.argmin(norma_toranja)

print(f'O minimo das laranjas é {minimo_laranja} e o minimo das toranjas é {minimo_toranja}')