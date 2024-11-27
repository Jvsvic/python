class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'{self._titular} | {self._saldo} | {self._ativo}  '



conta_1 = ContaBancaria('João', 1500) 
conta_2 = ContaBancaria('Paulo', 10000)
print(conta_1)
print(conta_2)