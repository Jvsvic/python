import pandas as pd  # Importa a biblioteca pandas para manipulação de dados.
import matplotlib.pyplot as plt  # Importa matplotlib para criar gráficos.

# URL do arquivo CSV contendo os dados.
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

# Lê o arquivo CSV e cria um DataFrame, usando ponto e vírgula (;) como separador.
dados = pd.read_csv(url, sep=';')
# Junta o TIPO e o BAIRRO e adiciona EM na coluna descricao
dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' +  dados['Quartos'].astype(str) + ' quartos ' +  ' e ' + dados['Vagas'].astype(str) + 'vagas de garagem'
print(dados.head())
dados.to_csv('colunas.csv', index=False)