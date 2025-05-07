# 17) Elaborar um programa que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias.

# Estou solicitando ao usuário quantos anos, meses e dias (ENTRADA)
anos = int(input("Quantos anos você tem? "))
meses = int(input("Quantos meses? "))
dias = int(input("Quantos dias? "))

# Aqui está convertendo esses números para dias totais (PROCESSO)
diasTotais = (anos * 365) + (meses * 30) + dias

# Aqui estou mostrando o resultado em dias totais para o usuário (SAÍDA)
print(f"Você já viveu {diasTotais} dias.")