# Notas do(a) estudante
notas = [8.5, 9.0, 6.0, 10.0]

def boletim(lista):
    media = sum(lista) / len(lista)
    
    if media >= 6:
        situacao = "Aprovado(a)"
    else:
        situacao = "Reprovado(a)"
    
    return (media, situacao)

resultado = boletim(notas)
print(resultado)