#lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]
#peso = [tupla[2] for tupla in lista_de_tuplas]

#print(f"peso: {peso}")


lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
print(f"{'Nome:':<10} {'Altura:':<10} {'Peso:':<10}")

for nome, altura, peso in lista_de_tuplas:
    print(f"{nome:<10} {altura:<10}{peso:<10}")



''''
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

terceiros_elementos = [tupla[2] for tupla in lista_de_tuplas]

print(terceiros_elementos)
'''