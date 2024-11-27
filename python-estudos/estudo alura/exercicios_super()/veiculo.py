from abc import ABC, abstractmethod
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f'Marca do veículo: {self.marca} | Modelo do veículo {self.modelo} | Status: Ligado'
    
    @abstractmethod
    def ligar(self):
        pass