aluguel = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
final = (aluguel*60) + (km * 0.15 )
print(f'O total a pagar é de {final:.2f}')