import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'
dados = pd.read_csv(url, sep=',')
print(dados.isnull().sum())
dados = dados.fillna(0)
print(dados.isnull().sum())