import pandas as pd  # Importa a biblioteca pandas para manipulação de dados.
import matplotlib.pyplot as plt  # Importa matplotlib para criar gráficos.

# URL do arquivo CSV contendo os dados.
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

# Lê o arquivo CSV e cria um DataFrame, usando ponto e vírgula (;) como separador.
dados = pd.read_csv(url, sep=';')

#Apartamentos que possuem pelo menos 2 quartos, aluguel menor que R$ 3000 e área maior que 70 metros quadrados.
selecao = (dados['Quartos'] >=2) & (dados['Valor'] < 3000) & (dados['Area'] > 70) & (dados['Tipo'] == 'Apartamento')
filtro = dados[selecao]

#print(filtro)
#Este comando cria um arquivo csv e retira a tabela unamed (sep=';' faz com que o separamento se torne com ;) 
dados.to_csv('filtro_apartamentos.csv', index=False)
print(pd.read_csv('filtro_apartamentos.csv'))