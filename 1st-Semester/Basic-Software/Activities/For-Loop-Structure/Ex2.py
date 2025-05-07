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