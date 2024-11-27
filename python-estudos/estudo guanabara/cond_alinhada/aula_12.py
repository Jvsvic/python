nome = str(input('Qual o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'José':
    print('Parabéns você está utilizando o metodo elif')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia {nome}')