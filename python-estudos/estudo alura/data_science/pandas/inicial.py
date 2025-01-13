import pandas as pd  # Importa a biblioteca pandas para manipulação de dados.

# URL do arquivo CSV com os dados de aluguel.
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

# Lê o arquivo CSV e cria um DataFrame. O separador do arquivo é o ponto e vírgula (;).
leitura = pd.read_csv(url, sep=';')

# Exibe o DataFrame completo no terminal (cuidado, pois pode ser muito grande).
print(leitura)

# Exibe as primeiras 11 linhas do DataFrame (10+1).
print(leitura.head(10+1))

# Exibe as últimas 5 linhas do DataFrame.
print(leitura.tail())

# Exibe o tipo de dado da variável `leitura` (deve ser pandas DataFrame).
print(type(leitura))

# Exibe o número de linhas e colunas no DataFrame no formato (linhas, colunas).
print(leitura.shape)

# Exibe o nome de todas as colunas do DataFrame.
print(leitura.columns)

# Mostra informações detalhadas sobre o DataFrame, incluindo tipos de dados e valores nulos.
print(leitura.info())

# Exibe apenas a coluna "Tipo" do DataFrame (uma Série do pandas).
print(leitura['Tipo'])

# Exibe as colunas "Quartos" e "Valor" como um novo DataFrame.
print(leitura[['Quartos', 'Valor']])
