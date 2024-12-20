#nota = float(input("Digite a nota do(a) estudante: "))
#
#def qualitativo(x):
#    return x + 0.5
#qualitativo(nota)
#return qualitativo(nota)

nota = float(input("Digite a nota do(a) estudante: "))
qualitativo = lambda x: x + 0.5
print(qualitativo(nota))
