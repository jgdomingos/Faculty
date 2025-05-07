# 7) Elaborar um algoritmo que leia 10 números. Logo após, deve exibir o menor valor lido e o maior valor lido.

numeros = []

for rep7 in range(1, 11):
    num = int(input("Digite um número: "))
    numeros.append(num)

print(f"Menor valor: {min(numeros)}")
print(f"Maior valor: {max(numeros)}")