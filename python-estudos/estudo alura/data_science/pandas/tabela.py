import pandas as pd  # Importa a biblioteca pandas para manipulação de dados.
import matplotlib.pyplot as plt  # Importa matplotlib para criar gráficos.

# URL do arquivo CSV contendo os dados.
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';')
dados['Valor_mes'] = dados['Valor'] + dados['Condominio']
dados['Valor_ano'] = dados['Valor_mes'] * 12 + dados['IPTU']
print(dados.head())