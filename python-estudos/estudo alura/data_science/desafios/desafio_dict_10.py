funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]
estado_funcionario = {}
soma_funcionario = {}
for estado in set(x[0] for x in funcionarios):
    lista = [x[1] for x in funcionarios if x[0] == estado]
    estado_funcionario[estado] = lista
    print([estado])
  

print(estado_funcionario)
