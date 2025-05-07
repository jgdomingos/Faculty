# 15) Elaborar um programa que leia três números inteiros (A, B, C) e calcule a seguinte expressão: D = R + S / 2 onde R = (A + B)2 e S = (B + C)2. Exibir o valor D.

# Nas 3 linhas a seguir estou solicitando ao usuário 3 números inteiros (ENTRADA)
numero1 = int(input("Qual o valor do número 1? "))
numero2 = int(input("Qual o valor do número 2? "))
numero3 = int(input("Qual o valor do número 3? "))

# Nas 3 linhas a segui esta calculado o valor de R, S e D (PROCESSO)
R = (numero1 + numero2) ** 2
S = (numero2 + numero3) ** 2
D = (R + S) / 2

# Aqui estou mostrando o resultado de D para o usuário (SAÍDA)
print(f"O valor de D é: {D}")