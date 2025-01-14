import pandas as pd 
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'
dados= pd.read_csv(url, sep=',')

#Aplicando filtro para alunos aprovados
selecao = (dados['Aprovado'] == True)
filtro = dados[selecao]
#Primeira opção
#filtro['Notas'] = filtro['Notas'].replace({7.0: '8.0'})
#Segunda Opção
filtro = filtro.replace(7.0, 8.0)
print(filtro)
filtro.to_csv('alunos_aprovados.csv', index=False)