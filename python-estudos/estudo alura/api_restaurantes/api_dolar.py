import requests
import json

url = "https://economia.awesomeapi.com.br/last/USD-BRL"
response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    cotacao = float(dados['USDBRL']['bid'])
    mensagem = f'U$ 1 dólar corresponde a R${cotacao:.2f}'
    print(mensagem)
else: 
    print('Error')