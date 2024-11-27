from estudo_importando import Livro

livro_biblioteca = Livro("Python in Practice", "Emily Coder", 2021)
print(f'Nome: {livro_biblioteca.titulo} Autor:{livro_biblioteca.autor} Antes de empresar o livro: {livro_biblioteca.disponivel} ')
livro_biblioteca.emprestar()
print(f'Nome: {livro_biblioteca.titulo}  Autor:{livro_biblioteca.autor} Depois de emprestar o livro: {livro_biblioteca.disponivel} ')
 
ano_especifico = 2020
livros_disponiveis = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis}")  