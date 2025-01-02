nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

total = list(map(lambda nome, sobrenome: (nome + ' ' + sobrenome).title().strip(), nomes, sobrenomes))
print(total)
completo = print(f'Nome completo: {total[1]} ')
