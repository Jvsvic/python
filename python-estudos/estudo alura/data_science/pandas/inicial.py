import pandas as pd
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
leitura = pd.read_csv(url, sep=';')
print(leitura)
print(leitura.head(10+1))
print(leitura.tail())
print(type(leitura))
print(leitura.shape)
print(leitura.columns)
print(leitura.info())
print(leitura['Tipo'])
print(leitura[['Quartos', 'Valor']])
