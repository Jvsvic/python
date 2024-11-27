print('O limite permitido é de 80KM/H')
vel = float(input('Qual a velocidade que estava na via: '))
if vel > 80:
    print('Você ultrapassou a velocidade da via.')
    multa = (vel-80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}')
else: 
    print('Você estava dentro da velocidade da via.')