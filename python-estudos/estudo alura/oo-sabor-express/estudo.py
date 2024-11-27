class Pessoa:
    def __init__(self, nome, idade, profissao):
        self._nome = nome.title()
        self._idade = idade
        self._profissao = profissao.title()

    def __str__(self):
        return f'{self._nome} | {self._idade} | {self._profissao}'

    @property
    def saudacao(self):
        if self._profissao:
            return f'Olá, sou {self._nome} e trabalho como {self._profissao}'
        else:
            pass

    def aniversario(self):
        self._idade += 1

pessoa_1 = Pessoa('João', 23, 'Estágiario')
print(pessoa_1.saudacao)
print(f'Idade de {pessoa_1._nome}: {pessoa_1._idade}')
print(f'Idade após aniversário: {pessoa_1._idade}')