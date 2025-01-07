import numpy as np
clientes = np.array([[1, 'João', 30, 'Rua A', 100, 'eletrônicos'],
                     [2, 'Maria', 25, 'Rua B', 200, 'moda'],
                     [3, 'Pedro', 35, 'Rua C', 50, 'esportes']])

intencao_compras = clientes[:,4:]
print(intencao_compras)