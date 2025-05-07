# 5) Elaborar um programa que leia o saldo de uma aplicação e imprimir o novo saldo, considerando um reajuste de 15%.

# Estou solicitando para o usuário o saldo antigo dele (ENTRADA)
saldo = float(input("Insira o seu antigo saldo: "))

# Aqui está sendo feito o calculo, na primeira linha está fazendo o saldo antigo * 0.15 e depois o resultado dessa multiplicação (reajuste) + o saldo antigo (PROCESSO)
reajuste = saldo * 0.15
novoSaldo = reajuste + saldo

# E aqui vai exibir o saldo atual já com o reajuste (SAÍDA)
print(f"O seu reajuste no saldo é de R${novoSaldo}")