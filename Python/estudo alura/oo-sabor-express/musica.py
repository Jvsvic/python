class Musica:
    nome = ''
    artista = ''
    duracao = int
musica_primeiro = Musica()
musica_primeiro.nome = 'Teste teste'
musica_primeiro.artista = 'Testando'
musica_primeiro.duracao = 355

musica_segundo = Musica()
musica_segundo.nome = 'Shape of You'
musica_segundo.artista = 'Ed Sheeran'
musica_segundo.duracao = 234

musica_terceiro = Musica()
musica_terceiro.nome = 'Imagine'
musica_terceiro.artista = 'John Lennon'
musica_terceiro.duracao = 183
musicas = [vars(musica_primeiro), vars(musica_segundo), vars(musica_terceiro)]
print(musicas)
