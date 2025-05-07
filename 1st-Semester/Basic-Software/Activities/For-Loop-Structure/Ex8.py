# 8) Elaborar um algoritmo que some todos os números inteiros abaixo de 1000 que são múltiplos de 3 ou 5

soma = sum(n for n in range(1000) if n % 3 == 0 or n % 5 == 0)
print(f"Soma dos múltiplos de 3 ou 5 abaixo de 1000: {soma}")