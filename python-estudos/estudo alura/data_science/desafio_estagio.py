frase = str(input('Digite uma frase: '))
frase = frase.replace('!', ' ').replace(',', ' ').replace('?', ' ').replace('.', ' ')
palavras = frase.split()
tamanho = list(filter(lambda x: len(x) >= 5, palavras))
print(list(tamanho))