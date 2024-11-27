from estudo_importando import Livro
        
livro1 = Livro("Aprendendo Python", "John Doe", 2022)
livro2 = Livro("Data Science Fundamentals", "Jane Smith", 2020)
livro3 = Livro('Teste um', 'João', 2024)

print(f'Nome: {livro3.titulo} Autor:{livro3.autor} Antes de empresar o livro: {livro3.disponivel} ')
livro3.emprestar() # Empresta um livro
print(f'Nome: {livro3.titulo}  Autor:{livro3.autor} Depois de emprestar o livro: {livro3.disponivel} ')

print(livro1)
print(livro2)
print(livro3)   