notas = [7]
tabuada = list(map(lambda x: x * notas[0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(tabuada)
for i in range(1, 11):
    print(f'{notas} x {i} = {notas[0] * i}')