nome = str(input('Qual o seu nome? '))
sobrenome = str(input('Qual seu sobrenome? '))
idade = int(input('Qual sua idade? '))
nascimento = int(input('Qual seu ano de nascimento?'))
altura = float(input('Qual sua altura?'))
if idade >= 18:
    print('É maior de idade!')
else: 
    print('É menor de idade!')
print(f'Meu nome é {nome}, tenho {idade} anos, nasci no ano de {nascimento} e tenho {altura} de altura')
