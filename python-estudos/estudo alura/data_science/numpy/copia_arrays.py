import numpy as np
preco_imoveis = np.array([10000,120000,11000,200000])
preco_imoveis_sao_paulo = np.copy(preco_imoveis)
preco_imoveis[0] = 120000
print(preco_imoveis_sao_paulo[0])
