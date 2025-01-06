id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]
resultado = [q * p for q, p in zip(quantidade, preco)]
print(f'{"ID":<10} {"Quantidade":<15} {"Preço":<10} {'Total':<10}')
for z,x,c,v in zip(id, quantidade, preco, resultado):
    print(f'{z:<10} {x:<15} {c:<10.2f} {v:<10}')


