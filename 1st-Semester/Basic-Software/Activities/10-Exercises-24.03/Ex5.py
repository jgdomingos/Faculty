# 5) Elaborar um algoritmo que receba os valores A, B, C e mostre na tela se a soma de A + B é menor que C

# Aqui estou solicitando os valores de A, B e C para o usuário (ENTRADA)
A = int(input("Digite um valor A: "))
B = int(input("Digite um valor B: "))
C = int(input("Digite um valor C: "))

# Aqui estou somando A e B (PROCESSO)
soma = A + B 

# Aqui está verificando se a soma de A e B é menor que C (CONDIÇÃO)
if (soma < C):
    print(F"A soma de A({A}) + B({B}) é menor que C({C})") # (SAÍDA)
else:
    print(F"A soma de A({A}) + B({B}) é maior que C({C})") # (SAÍDA)