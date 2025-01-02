from random import randrange
participantes_totais = int(input('Quantos participantes tem no total? '))
for i in range(participantes_totais):
    sorteado = randrange(participantes_totais)
print(sorteado)