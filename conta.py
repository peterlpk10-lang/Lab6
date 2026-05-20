class Conta:
    def __init__(self, nome):
        self.__nome = nome
        self.__saldo = 0
    
    def sacar(self, valor_saque):
        self.__saldo -= valor_saque

    def depositar(self, valor_deposito):
         self.__saldo += valor_deposito

    def calcular_rendimento(self):
        return self.__saldo * 0.1

    def mostrar_saldo(self):
        print(f"SALDO ATUAL: R${self.__saldo}")

