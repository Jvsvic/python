import pandas as pd  # Importa a biblioteca pandas para manipulação de dados.
import matplotlib.pyplot as plt  # Importa matplotlib para criar gráficos.

# URL do arquivo CSV contendo os dados.
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

# Lê o arquivo CSV e cria um DataFrame, usando o ponto e vírgula (;) como separador.
dados = pd.read_csv(url, sep=';')

# Exibe a quantidade de valores ausentes (NaN) em cada coluna.
print(dados.isnull().sum())

# Substitui valores ausentes (NaN) por 0.
dados = dados.fillna(0)

# Verifica novamente se há valores ausentes após a substituição.
print(dados.isnull().sum())
