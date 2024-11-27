from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas, cor):
        super().__init__(marca, modelo)
        self.portas = portas
        self.cor = cor

    def __str__(self):
        return f'Marca do veículo: {self.marca} | Modelo do veículo {self.modelo} | Quantidade de portas: {self.portas} | Cor: {self.cor} | Status: Ligado'