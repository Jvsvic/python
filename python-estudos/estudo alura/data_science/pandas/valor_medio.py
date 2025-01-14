import pandas as pd  # Importa a biblioteca pandas para manipulação de dados.
import matplotlib.pyplot as plt  # Importa matplotlib para criar gráficos.

# URL do arquivo CSV contendo os dados.
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

# Lê o arquivo CSV e cria um DataFrame, usando ponto e vírgula (;) como separador.
dados = pd.read_csv(url, sep=';')

# print(dados.head())  
# Este comando (comentado) exibiria as primeiras 5 linhas do DataFrame `dados`.

# print(dados['Valor'].mean())  
# Este comando (comentado) exibiria a média dos valores na coluna 'Valor'.

# Calcula a média dos valores de aluguel por tipo de imóvel e ordena por valor.
# preco = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

# Plota o gráfico de barras horizontais com os preços médios.
# preco.plot(kind='barh', figsize=(14, 10), color='purple');
# plt.show()  
# Este comando (comentado) exibe o gráfico dos valores médios por tipo de imóvel.

# Exibe os tipos únicos de imóveis no DataFrame.
#print(dados.Tipo.unique())

# Lista de tipos de imóveis comerciais.
imoveis_comerciais = ['Conjunto Comercial/Sala', 'Prédio Inteiro', 'Loja/Salão', 
                      'Galpão/Depósito/Armazém', 'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial', 'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio', 'Pousada/Chalé', 
                      'Hotel', 'Indústria']

# Filtra o DataFrame para remover os tipos de imóveis comerciais.
# Mantém apenas os tipos de imóveis residenciais.
df = dados.query('@imoveis_comerciais not in Tipo')

# Calcula a média dos valores de aluguel por tipo de imóvel e ordena por valor.
preco = df.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

# print(df.Tipo.unique())  
# Este comando (comentado) exibiria os tipos de imóveis residenciais restantes no DataFrame.

# Plota o gráfico de barras horizontais com os preços médios dos imóveis residenciais.
# preco.plot(kind='barh', figsize=(14, 10), color='purple');
# plt.show()  
# Este comando (comentado) exibe o gráfico com os preços médios por tipo de imóvel.

# Calcula o percentual de imóveis por tipo no DataFrame.
df_percentual = df['Tipo'].value_counts(normalize=True).to_frame().sort_values('Tipo')

# Plota um gráfico de barras mostrando o percentual de cada tipo de imóvel.
df_percentual.plot(kind='bar', figsize=(14, 10), color='green', edgecolor='black',
                   xlabel='Tipos', ylabel='Percentual');
# plt.show()  
# Este comando (comentado) exibe o gráfico de barras com os percentuais.

# Renomeia a coluna de 'proportion' para 'Percentuais' no DataFrame.
df_percentual.rename(columns={'proportion': 'Percentuais'}, inplace=True)

# Filtra o DataFrame para incluir apenas imóveis do tipo 'Apartamento'.
df = df.query('Tipo == "Apartamento"')

# Exibe as primeiras 5 linhas do DataFrame filtrado.
#print(df.head())

# Calcula o percentual de imóveis do tipo 'Apartamento'.
df_percentual_tipo = df['Tipo'].value_counts(normalize=True).to_frame().sort_values('proportion')

# Salvando o DataFrame em uma variável.
df_exemplo = df['Tipo'].value_counts(normalize=True).to_frame().sort_values('Tipo')

# Renomeia a coluna 'proportion' para 'Percentuais'.
df_exemplo.rename(columns={'proportion': 'Percentuais'}, inplace=True)

# Visualizando o DataFrame.
# print(df_exemplo)  
# Este comando (comentado) exibiria o DataFrame final com os percentuais de imóveis do tipo 'Apartamento'.
