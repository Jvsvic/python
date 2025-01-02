nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]
nome = [nome[0] for nome in nomes]
print(nome)
estudantes = list(zip(nomes,medias))

candidatos = [estudante[0] for estudante in estudantes if estudante[1] >= 8.0]

candidatos = list(zip(nomes,medias))
print([candidatos[1]]) 