# 4) Elaborar um algoritmo que lê 20 números inteiros. Para cada número inserido exibir se é par ou ímpar.
 
for rep4 in range(1,21):
    num = int(input("Digite um número "))
    if (num % 2 == 0):
        print("O número é par")
    else:
        print("O número é impar")