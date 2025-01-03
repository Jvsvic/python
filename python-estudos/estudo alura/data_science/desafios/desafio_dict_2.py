#lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

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