from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/api/hello")
def hello_world():
    '''
    Endpoint que exibe uma mensagem incrivel do mundo da programação
    '''
    return {"Hello": "World"}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    # Verificação do status da resposta, agora dentro da função
    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante = []
        # Para cada item dentro de dados_json
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'], 
                    "description": item['description']
                })
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}

    else:
        # Retorno de erro adequado em caso de falha na requisição
        return {"Erro": "Não foi possível obter os dados dos restaurantes", "status_code": response.status_code}
