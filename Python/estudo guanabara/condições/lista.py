import random
escolher = int(input('Escolha um número: '))
lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista)
print(f'O número escolhido foi {escolhido}')
if escolher == escolhido:
    print('Parabéns você acertou!')
else:
    print('Você errou! Tente novamente.')
