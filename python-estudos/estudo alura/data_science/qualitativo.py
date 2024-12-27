# Notas do(a) estudante
notas = [6.0, 7.0, 9.0, 5.5, 8.0]
qualitativo = 0.5
notas_atualizadas = list(map(lambda x: x + qualitativo, notas))

print(notas_atualizadas)