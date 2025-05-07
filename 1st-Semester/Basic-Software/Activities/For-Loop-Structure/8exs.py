# 1) Elaborar um algoritmo que leia um valor de temperatura em graus Celsius, calcule e exiba a temperatura equivalente em Kelvin, sabendo que: K = C + 273. Esse algoritmo deve repetir 5 vezes
 
for rep in range(1,6):
    celsius = int(input("Qual a temperatura em Censius? "))
    K = celsius + 273
    print(K)
 
 
# 2) Elaborar um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este número é múltiplo de 3 e se é positivo ou negativo. Esse programa deve-se repetir 6 vezes esse processo.
 
for rep2 in range(1,7):
    num1 = int(input("Qual o número inteiro? "))
    multiplo = num1 % 3
    if (multiplo == 0):
        print("O número é multiplo de 3")
        if (num1 > 0):
            print("Esse número tambem é positivo")
        else:
            print("Esse número é negativo")
    else:
        print("O número não é multiplo de 3")
   
# 3) Elaborar um algoritmo que recebe 3 valores (A, B e C) e exibe qual é o maior entre eles. Esse programa deve-se repetir 20 vezes
 
for rep3 in range(1,21):
    A = float(input("Qual o valor de A? "))
    B = float(input("Qual o valor de B? "))
    C = float(input("Qual o valor de C? "))
    if (A > B and A > C):
        print(f"A é o maior valor {A}")
    elif(B > A and B > C):
        print(f"B é o maior valor {B}")
    elif (C > A and C > B):
        print(f"C é o maior valor {C}")
    else:
        print("Os valores são iguais")
 
# 4) Elaborar um algoritmo que lê 20 números inteiros. Para cada número inserido exibir se é par ou ímpar.
 
for rep4 in range(1,21):
    num = int(input("Digite um número "))
    if (num % 2 == 0):
        print("O número é par")
    else:
        print("O número é impar")
 
# 5) Elaborar um algoritmo que solicita ao usuário para digitar 15 valores e deve exibir a soma e média.
 
dados = []
 
for rep5 in range(1,16):
    numero = float(input("Qual o número? "))
    valores = dados.append(numero)
 
soma = sum(dados)
media = soma / 15
print(f"A soma desses número é {soma} e a média é {media}")
 
# 6) Elaborar um algoritmo que o usuário tenha que digitar 10 números inteiros. No final, o programa deve exibir quantos números são múltiplos de 3, quantos números são menores que 45 e maiores que 55, e qual é o menor número entre eles
 
valores = []
 
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    valores.append(num)

multiplos3 = sum(1 for n in valores if n % 3 == 0)
entre45e55 = sum(1 for n in valores if n < 45 or n > 55)
menorNumero = min(valores)

print(f"Quantidade de múltiplos de 3: {multiplos3}")
print(f"Quantidade de números menores que 45 e maiores que 55: {entre45e55}")
print(f"Menor número digitado: {menorNumero}")


# 7) Elaborar um algoritmo que leia 10 números. Logo após, deve exibir o menor valor lido e o maior valor lido.

numeros = []

for rep7 in range(1, 11):
    num = int(input("Digite um número: "))
    numeros.append(num)

print(f"Menor valor: {min(numeros)}")
print(f"Maior valor: {max(numeros)}")

# 8) Elaborar um algoritmo que some todos os números inteiros abaixo de 1000 que são múltiplos de 3 ou 5

soma = sum(n for n in range(1000) if n % 3 == 0 or n % 5 == 0)
print(f"Soma dos múltiplos de 3 ou 5 abaixo de 1000: {soma}")