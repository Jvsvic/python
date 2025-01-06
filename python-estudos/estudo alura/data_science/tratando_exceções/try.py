def media(lista: list = None) -> float:
    if lista is None:
        lista = [0]  # Definir lista padrão para evitar erro de tipo
    if len(lista) > 4:
        raise ValueError('A lista não pode possuir mais de 4 notas')
    if len(lista) == 0:
        raise ValueError('A lista não pode estar vazia')
    calculo = sum(lista) / len(lista)
    return calculo

try:
    notas = [6, 7, 8, 9,1]
    resultado = media(notas)
except TypeError:
    print("Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!")
except ValueError as e:
    print(e)
else:
    print(resultado)
finally:
    print("A consulta foi encerrada!")