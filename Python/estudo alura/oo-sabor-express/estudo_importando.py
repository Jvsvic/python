import os
class Livro:
    lista_de_livros = []  
    
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.lista_de_livros.append(self)


    def __str__(self):
        return f"Livro: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao}"

    def emprestar(self):
        self.disponivel = False #Usar ele muda o disponivel para FALSE


    @staticmethod        
    def verificar_disponibilidade(ano):
        livros_disponiveis = [item for item in Livro.lista_de_livros if item.ano_publicacao == ano and item.disponivel]
        return livros_disponiveis   
0