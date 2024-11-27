class Musica:
    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'

    def listar():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')


# Criando instâncias de Musica
musica_1 = Musica('Teste', 'Testando', 355)
musica_2 = Musica('Shape of You', 'Ed Sheeran', 234)
musica_3 = Musica('Imagine', 'John Lennon', 183)

# Chamando o método de classe para listar todas as músicas
Musica.listar()
