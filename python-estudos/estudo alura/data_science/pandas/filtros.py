import pandas as pd  # Importa a biblioteca pandas para manipulação de dados.
import matplotlib.pyplot as plt  # Importa matplotlib para criar gráficos.

# URL do arquivo CSV contendo os dados.
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

# Lê o arquivo CSV e cria um DataFrame, usando ponto e vírgula (;) como separador.
dados = pd.read_csv(url, sep=';')

#Filtro de Apartamentos com 1 quarto e aluguel menor que 1200
selecao1 = (dados['Quartos'] == 1)
(dados[selecao1])
selecao2 = dados['Valor'] < 1200
(dados[selecao2])
selecao3 = (dados['Tipo'] == 'Apartamento') 
#Junta as três seleções em uma só
selecao_final = (selecao1) & (selecao2) & (selecao3)
print(dados[selecao_final])