from restaurante import Restaurante
from bebida import Bebida
from prato import Prato
from sobremesa import Sobremesa
restaurante_praca = Restaurante('Praça', 'Gourmet')
suco = Bebida('Suco de Melancia', 5.0, 'Grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()
sobremesa1 = Sobremesa('Canjica', 10.00, 'Doce', 'Grande', 'Um docinho pra alegrar seu dia')
restaurante_praca.adicionar_cardapio(suco)
restaurante_praca.adicionar_cardapio(prato_paozinho)
restaurante_praca.adicionar_cardapio(sobremesa1)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()

# AQUI ARMAZENA TODOS OS DADOS INSERIDOS