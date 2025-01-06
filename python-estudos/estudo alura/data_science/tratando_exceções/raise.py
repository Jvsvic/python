def media(lista: list = None) -> float:
    if lista is None:
        lista = [0]  # Definir lista padrão para evitar erro de tipo
    if len(lista) > 4:
        raise ValueError('A lista não pode possuir mais de 4 notas')
    if len(lista) == 0:
        raise ValueError('A lista não pode estar vazia')
    calculo = sum(lista) / len(lista)
    return calculo

notas = []
resultado = media(notas)
print(resultado)
