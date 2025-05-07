# 6) Elaborar um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.

# Estou solicitando o salário atual e o percentual de aumento (ENTRADA)
salario = float(input("Insira seu salário atual: "))
percentual = float(input("Insira qual foi o percentual de aumento: "))

# Aqui está sendo feita a resolução do problema (PROCESSO)
reajuste = salario * (percentual / 100)
novoSalario = salario + reajuste

# Aqui vai exibir o novo salário e o reajuste desse funcionário (SAÍDA)
print(f"Você teve um aumento salarial de R${reajuste} o valor do seu novo salário é de R${novoSalario}")