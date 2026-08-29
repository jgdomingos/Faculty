class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo #protegido

    def mostrar_saldo(self):
        print("O valor do seu saldo é:" , self._saldo)

    def sacar(self, valor):
        if valor > self._saldo:
            print("Saldo insulficiente!")
        else:
            self._saldo -= valor

    def deposito(self, valor):
        self._saldo += valor

cliente1 = ContaBancaria("João", 5000)

print("Opções do menu:\n")
print("Digite 1 - Sacar")
print("Digite 2 - Depositar")

opcaoDesejada = input("Digite o valor desejado:")

if opcaoDesejada == "1":
    valor = float(input("Digite o valor do saque: "))
    cliente1.sacar(valor)
elif opcaoDesejada == "2":
    valor = float(input("Digite o valor do deposito: "))
    cliente1.deposito(valor)
else:
    print("Opção inválida, digite uma opção válida!")

cliente1.mostrar_saldo()