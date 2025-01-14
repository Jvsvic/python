import pandas as pd 
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'
dados= pd.read_csv(url, sep=',')
remove = dados.query('Nome == "Carlos" | Nome == "Alice"').index 
print(remove) 
dados.drop(remove, axis=0, inplace=True)
print(dados)