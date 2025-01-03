aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
apartamento = [(tupla[1], 'Apartamento') for tupla in aluguel if tupla[0] == 'Apartamento'] 


#Retorna os valores
print(apartamento)