#Notas do(a) estudante
notas = {'19 Trimestre': 8.5, '2° Trimestre': 9.5, '3º trimestre': 7}
soma = 0 
for nota in notas.values():
    soma += nota
    somatorio = sum(notas.values())
    print(somatorio) ##
    print(soma)
    qtd_notas = len(notas)
    print(qtd_notas)

media = somatorio / qtd_notas
media = round(media,1)
print(media)