import pandas as pd  # Importa a biblioteca pandas para manipulação de dados.
import matplotlib.pyplot as plt  # Importa matplotlib para criar gráficos.

# URL do arquivo CSV contendo os dados.
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

# Lê o arquivo CSV e cria um DataFrame, usando o ponto e vírgula (;) como separador.
dados = pd.read_csv(url, sep=';')
###########################################################################
registros_a_remover = dados.query('Valor == 0 | Condominio == 0').index
#Esse codigo filtra os valores 0 das duas colunas acima
print(registros_a_remover)
#Esse codigo mostra quantas linhas temos com esse problema
dados.drop(registros_a_remover, axis=0, inplace=True)
 # Esse codigo executa o drop, alem de axis0 indentifica que é somente para dropar linhas