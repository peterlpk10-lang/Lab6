class Conta:
    def __init__(self):
        self.__saldo = 0
    
    def saca(self, valor_saque):
        self.__saldo -= valor_saque

    def deposita(self, valor_deposito):
         self.__saldo += valor_saque

    def calcula_rendimento(self):
        return self.__saldo * 0.1

    def mostra_saldo(self):
        print(f"Saldo: {self.__saldo}")

