idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}
try:
    pesquisador = input('Digite um nome dentro do banco de dados: ').title()
    resultado = idades[pesquisador]
except KeyError:
    print(f'O nome {pesquisador} não existe no banco de dados')
else:
    print(resultado)