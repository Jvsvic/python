sal = float(input('Escreva seu salário: '))
if sal > 1250:
    aumento = sal+(sal * 10 / 100)
    print(f'O salário com reajuste será: {aumento:.2f}')
else:
    quinze = sal+(sal * 15 / 100)
    print(f'O salário com reajuste será: {quinze:.2f}')