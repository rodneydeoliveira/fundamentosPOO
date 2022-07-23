class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print(f'O saldo de {self.__titular} é de R${self.__saldo}.')

    def deposita(self, valor):
        self.__saldo += valor
        print (f'Houve um depósito de {valor}')
        return self.__saldo

    """def __pode_sacar(self, valor_do_saque):
        valor_disponivel_a_sacar = self.saldo + self.limite
        return valor_do_saque <= valor_disponivel_a_sacar"""

    def saca(self, valor):

        # saldo suficiente
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f'Houve um saque de {valor}')

        # saldo está positivo, mas não vai ser suficiente
        # garante que o saldo está positivo para não interferir na soma com o limite
        elif valor > self.__saldo and self.__saldo > 0 and valor <= (self.__saldo + self.__limite):
            diferenca = valor - self.__saldo
            self.__saldo -= valor
            self.__limite -= diferenca
            print(f'Houve um saque de {valor}, porém seu saldo ficou negativo, então seu limite foi reduzido.')

        # saldo negativo mas limite suficiente
        elif self.__saldo < 0 and valor <= self.__limite:
            self.__limite -= valor
            self.__saldo -= valor
            print(f'Houve um saque de {valor}, como seu saldo está negativo, seu limite foi reduzido')

        # nem saldo nem limite suficientes
        else:
            print("Você não tem limite suficiente!")

    def transfere(self, valor, destino):
        self.destino = destino
        self.saca(valor)
        destino.deposita(valor)
    @property
    def saldo(self):#Get é usado para ter o retorno de algo, sempre!
        return self.__saldo

    @property
    def titular(self):
        return self.__titular.title()

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):# Set é usado para acessar um attibuto, e modificá-lo
        self.__limite = limite
# Apenas criar os métodos GET E SET quando forem realmente necessários...
    @staticmethod# São métodos pertencentes à classe, não ao objeto. Podemos acessá-los sem a necessidade
                 # de instanciarmos um objeto.
    def codigos_dos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}
    @staticmethod
    def codigo_do_banco():
        return "001"




conta = Conta(2565, "Rodney", 55.0, 1000.0)
conta2 = Conta(123, "Nico", 180.0, 1000.0)
conta.extrato()
conta2.extrato()

conta.transfere(25.0, conta2)

conta.extrato()
conta2.extrato()
