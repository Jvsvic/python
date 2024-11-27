from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo) # Chama o construtor da classe base
        self.tipo = tipo

    def __str__(self):
        return f'Marca do veículo: {self.marca} | Modelo do veículo {self.modelo} | {self.tipo} | Status: Ligado'# Chama o construtor da classe base