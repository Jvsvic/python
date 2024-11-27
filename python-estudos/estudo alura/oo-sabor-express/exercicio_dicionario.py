pessoa = [{'nome':'João', 'idade':'23', 'cidade':'São Paulo'}]

pessoa[0]['idade'] = 40
pessoa[0]['profissao'] = 'vendedor'
del pessoa[0]['cidade']
print(pessoa)
chave = 'nome'
if chave in pessoa[0]:
    print('Tem a chave requerida')
else:
    print('Não tem a chave requerida')
    

