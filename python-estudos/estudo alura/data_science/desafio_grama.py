import math

raio = float(input('Entre com o raio da área que deseja orçar: '))

area = (math.pi*pow(raio, 2))

preco = area * 25
print(f'O orçamento para {area:.2f}m² é R${preco:.2f}')