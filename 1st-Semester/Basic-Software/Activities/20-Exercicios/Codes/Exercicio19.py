# 19) Elaborar um programa que calcule o salário líquido de um funcionário, exibindo no final o nome, telefone e o salário líquido, considerando:
# a) os dados do funcionário: nome, RG e telefone.
# b) salário bruto de R$ 2500,00
# c) descontos de R$ 300,00

# Estou solicitando dados pessoais para o usuário (ENTRADA)
nome = input("Qual o seu nome completo? ")
rg = input("Qual o seu RG? ")
telefone = input("Qual o seu número de telefone? ")

# Estou fornecendo ao sistema o salário bruto e o valor do desconto
salarioBruto = 2500.00
desconto = 300.00

# Aqui está calculando o valor so salário líquido do funcionário (PROCESSO)
salarioLiquido = salarioBruto - desconto

# Aqui está mostrando os dados pessoais cadastrados e o salário líquido para o usuário (SAÍDA)
print(f"Nome: {nome}\nRG: {rg}\nTelefone:{telefone}\nSalário Líquido: R${salarioLiquido}")