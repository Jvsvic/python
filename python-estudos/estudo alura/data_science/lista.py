from random import randrange, sample

lista = []

for i in range(0, 20):
  lista.append(randrange(100))

resultado = sample(lista, 5)

print(lista)
print(resultado)

