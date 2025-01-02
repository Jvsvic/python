notas = [8.5, 9.0, 6.0, 10.0]
def media(lista):
    calculo = sum(lista) / len(lista)
    calculo = round(calculo, 1)
    print(calculo)
media(notas)    