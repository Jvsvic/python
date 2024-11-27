import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url) 
print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}

    #para cada item dentro de dados_json
    for item in dados_json:
        # O nome do restaurante vai ser o item 'Company'
        nome_do_restaurante = item['Company']
        # Verificar se o nome do restaurante já apareceu
        # Se o nome do restaurante não estiver em dados_restaurante, cria uma lista vazia
        if nome_do_restaurante not in dados_restaurante:
            #criar uma lista com todas as informacoes
            dados_restaurante[nome_do_restaurante] = []

# Adiciona o item, preço e descrição à lista do restaurante
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'], 
            "description": item['description']
        })
else:
    print('Erro')

for nome_do_restaurante, dados in dados_restaurante.items():
    nome_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)
