notas = []
for i in range(5):
    nota = float(input(f'Digite a nota {i+1}: '))
    notas.append(nota)
print(notas)

notas.remove(max(notas))
notas.remove(min(notas))
media = sum(notas) / len(notas)
print(f'A media das notas foi {media}')
