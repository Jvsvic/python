import pandas as pd  # Importa a biblioteca pandas para manipulação de dados.
import matplotlib.pyplot as plt  # Importa matplotlib para criar gráficos.

# URL do arquivo CSV contendo os dados.
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

# Lê o arquivo CSV e cria um DataFrame, usando ponto e vírgula (;) como separador.
dados = pd.read_csv(url, sep=';')

# Comentário original:
# print(dados.columns)  
# Aqui eu visualizei as colunas e identifiquei 'Quartos'.

# print(dados.Quartos.unique())  
# Mostra os valores únicos na coluna 'Quartos' para entender melhor os dados.

# Lista de tipos de imóveis comerciais (e alguns outros que serão filtrados do DataFrame).
imoveis_comerciais = ['Conjunto Comercial/Sala', 'Prédio Inteiro', 'Loja/Salão', 
                      'Galpão/Depósito/Armazém', 'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial', 'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio', 'Pousada/Chalé', 
                      'Hotel', 'Indústria', 'Quitinete', 'Casa de Vila', 
                      'Studio', 'Loft', 'Flat', 'Casa', 'Casa de Condomínio']

# Filtra o DataFrame para manter apenas os imóveis que NÃO estão na lista de comerciais.
df = dados.query('@imoveis_comerciais not in Tipo')

# Calcula a média de quartos entre os imóveis restantes.
preco = df['Quartos'].mean()

# Outra forma de calcular a média de quartos.
df_media = df['Quartos'].mean()

# print(preco)  
# Mostra a média de quartos calculada.

# print(df_media)  
# Mostra novamente a média de quartos, calculada de outra forma.

# Calcula a média de quartos apenas para imóveis do tipo 'Apartamento'.
media = dados[dados['Tipo'] == 'Apartamento']['Quartos'].mean()  

# Comentário original:
# print(media)  
# Mostra a média de quartos nos imóveis do tipo 'Apartamento'.

# Exibe os bairros únicos presentes no DataFrame.
# print(dados['Bairro'].unique())  

# Ordena os dados pelo valor de aluguel, do maior para o menor.
# bairros = dados.sort_values('Valor', ascending=False)

# Exibe apenas as colunas 'Bairro' e 'Valor' do DataFrame.
# print(dados[['Bairro', 'Valor']])

# Calcula o valor médio de aluguel por bairro, ordena do maior para o menor, 
# e seleciona apenas os 5 primeiros (com os valores mais altos).
valor_alto = dados.groupby('Bairro')[['Valor']].mean().sort_values('Valor', ascending=False).head()

# Exibe os 5 bairros com os valores médios de aluguel mais altos.
print(valor_alto)

# Plota um gráfico de barras horizontais mostrando os 5 bairros com aluguel mais alto.
valor_alto.plot(kind='barh', figsize=(14, 10), color='blue');

# Exibe o gráfico.
plt.show()
