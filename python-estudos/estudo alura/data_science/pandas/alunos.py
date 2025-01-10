import pandas as pd
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'
dados = pd.read_csv(url, sep=',')
#print(dados)
print(dados.head(7))
print(dados.tail(5))
print(dados.shape)
print(dados.columns)
print(dados[['Nome', 'Idade']])
print(dados.dtypes)
print(dados.describe())