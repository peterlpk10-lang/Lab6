class Conta:
    def __init__(self):
        self.__saldo = 0
    
    def sacar(self, valor_saque):
        self.__saldo -= valor_saque

    def depositar(self, valor_deposito):
         self.__saldo += valor_saque

    def calcular_rendimento(self):
        return self.__saldo * 0.1

    def mostrar_saldo(self):
        print(f"Saldo: {self.__saldo}")

