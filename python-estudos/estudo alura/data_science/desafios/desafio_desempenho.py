nota = []
for i in range(5):
    calculo = float(input(f'Digite a {i+1} nota: '))
    nota.append(calculo)

print(nota)
maior = max(nota)
menor = min(nota)
media = sum(nota) / len(nota)
print(f'A media das notas foi {media}, a maior nota foi {maior} e a menor nota foi {menor}')

if media >= 6:
    print('Aprovado')
else:
    print('Reprovado')