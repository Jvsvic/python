lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]
soma = sum(sum(i) for i in lista_de_listas)
print(soma)