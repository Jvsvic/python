from math import sqrt 

numeros = [2, 8, 15, 23, 91, 112, 256]

for number in numeros:
    raiz = sqrt(number)
    if raiz.is_integer():
        print(f'A raiz de {number:.2f} é {raiz:.2f} e é inteira.')
    else:
        print(f'A raiz de {number:.2f} é {raiz:.2f} e não é inteira')