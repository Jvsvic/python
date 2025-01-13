import pandas as pd  # Importa a biblioteca pandas para manipulação de dados.

# URL do arquivo CSV contendo os dados dos alunos.
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

# Lê o arquivo CSV e cria um DataFrame. O separador usado no arquivo é a vírgula (`,`).
dados = pd.read_csv(url, sep=',')

# Exibe as primeiras 7 linhas do DataFrame.
print(dados.head(7))

# Exibe as últimas 5 linhas do DataFrame.
print(dados.tail(5))

# Exibe a quantidade de linhas e colunas no DataFrame no formato (linhas, colunas).
print(dados.shape)

# Exibe os nomes de todas as colunas do DataFrame.
print(dados.columns)

# Exibe apenas as colunas "Nome" e "Idade" como um novo DataFrame.
print(dados[['Nome', 'Idade']])

# Mostra os tipos de dados de cada coluna no DataFrame.
print(dados.dtypes)

# Exibe estatísticas descritivas sobre as colunas numéricas do DataFrame.
print(dados.describe())
