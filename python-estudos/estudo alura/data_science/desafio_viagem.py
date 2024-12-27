cidades = ['Salvador', 'Fortaleza', 'Natal', 'Aracaju']
hotel = 150
gasolina = 5
dia = 1
km_por_litro = 14
comida = [200, 400, 250, 300]
km = [850, 800, 300, 550]
distancia = km[0]


def gasto_hotel():
    dias_hotel = int(input('Quantos dias você irá ficar no hotel? '))
    custo_hotel = dias_hotel * hotel
    print(f'Custo do hotel: R${custo_hotel}')
    return dias_hotel

def gasto_gasolina():
    consumo = distancia / km_por_litro
    custo_gasolina = consumo * gasolina
    print(f'Custo de gasolina: R${custo_gasolina:.2f}')

def gasto_passeio(dias, cidade):
    # Usando o índice da cidade para acessar o custo da comida
    indice_cidade = cidades.index(cidade)
    custo_passeio = comida[indice_cidade] * dias
    print(f'Custo de passeios e alimentação em {cidade}: R${custo_passeio:.2f}')

dias = gasto_hotel()
gasto_gasolina()

cidade = cidades[0]  # Exemplo: Salvador
gasto_passeio(dias, cidade)





