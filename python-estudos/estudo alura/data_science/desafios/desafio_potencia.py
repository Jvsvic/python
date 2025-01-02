from math import pow
txtone = int(input('Digite um número inteiro: '))
txttwo = int(input('Digite outro número inteiro: '))
potencia = pow(txtone,txttwo)
print(f'A potencia do {txtone} elevado ao {txttwo} é {potencia}')
continuar = str(input('Deseja continuar? S/N ')).strip().upper()
if continuar == 'S':
    txtone = int(input('Digite um número inteiro: '))
    txttwo = int(input('Digite outro número inteiro: '))
    potencia = pow(txtone,txttwo)
    print(f'A potencia do {txtone} elevado ao {txttwo} é {potencia}')
else:
    print('Até logo.')

