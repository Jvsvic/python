import os 
from avaliacao import Avaliacao
from item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = [] # Lista de todos os restaurantes criados

    def __init__(self, nome, categoria): 
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False #_ define o controle interno
        self._avaliacao = [] #Recebe uma lista de avaliacoes
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome.ljust(25)} | {self.categoria} | {self.ativo}'
    
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'  # 

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if nota <= 0 or nota > 5:
            print('Insira um valor de 0 a 5 como nota')
        else:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)            


    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Ainda não tem avaliações'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) #Soma todas as notas
        quantidade_notas = len(self._avaliacao) #Le todas as notas 
        media = round(soma_das_notas / quantidade_notas, 1) # round arredonda a nota // SOMA E DIVIDE 
        return media
    

    def adicionar_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)


    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._cardapio} \n')
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Descrição {item.descricao}'
                print(mensagem_prato)
            elif hasattr:
                mensagem_bebida = f'{i}. Nome:{item._nome} |Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
            else: 
                mensagem_sobremesa = f'{i}. Nome:{item._nome} |Preço: R${item._preco} | Tipo: {item.tipo} | Tamanho: {item.tamanho} | Descrição: {item.descricao}'
                print(mensagem_sobremesa)


    @classmethod
    def listar_restaurantes(cls):
        os.system('cls')
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)}| {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')


    