from random import choice

frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]
escolhidas = []

for i in range(0,3):
    escolhida = choice(frutas)
    escolhidas.append(escolhida)
print(f'A salada de frutas vai conter as frutas: {', '.join(escolhidas)}')