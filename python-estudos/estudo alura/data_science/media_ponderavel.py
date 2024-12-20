notas = []
for i in range(0,3):
    notas.append(float(input('Digite a nota do estudante: ')))
media_ponderavel = lambda x, y, z: (x * 3 + y * 2 + z * 5) / 10
media_estudante = media_ponderavel(notas[0], notas[1], notas[2])
print(f'A média ponderada do estudante é: {media_estudante}')