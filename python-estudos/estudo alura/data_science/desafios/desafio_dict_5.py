meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]
print(f'{'Mes':<10} {'Despesa':<10}')
for mes, valores in zip(meses, despesa):
    print(f'{mes:<10} {valores:<10}')