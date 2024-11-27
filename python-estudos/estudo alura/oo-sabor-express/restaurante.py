class Restaurante: 
    nome = ''
    categoria = ''
    ativo = False
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'
nome_restaurante = restaurante_praca.nome
categoria = restaurante_praca.categoria
restaurante_praca.nome = 'Bistrô'
if restaurante_praca.ativo == True:
    print('O restaurante está ativado.')
else:
    print('O restaurante está desativado.')



restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
if restaurante_pizza.categoria == 'Fast Food':
    print('O restaurante é Fast Food')
else:
    print('O restaurante não é Fast Food')
restaurante_pizza.ativo = True

print(f'Nome: {restaurante_praca.nome}\n Categoria: {restaurante_praca.categoria}')
restaurantes = [restaurante_praca, restaurante_pizza]
print(vars(restaurante_praca))
