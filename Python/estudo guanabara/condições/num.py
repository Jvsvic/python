n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva outro número: '))
n3 = int(input('Escreva o últumo número: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print(f'O menor valor digitado foi: {menor}')
print(f'O maior valor digitado foi: {maior}')