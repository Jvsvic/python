estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']
estados_unicos = list(set(estados))
filiais = {estados_unicos[i]: estados.count(estados_unicos[i]) for i in range (len(estados_unicos))}
print(filiais)