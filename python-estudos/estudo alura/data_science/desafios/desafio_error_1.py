try:
    num_o = float(input('Digite um número: '))
    num_t = float(input('Digite outro número: '))
    divisao = num_o / num_t
    print(divisao)
except Exception as e:
    print(type(e), f'Erro: {e}')