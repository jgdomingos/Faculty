# 2) Elabore um algoritmo que calcule a soma de dois números quaisquer e apresente na tela 0 resultado dessa soma. Caso a soma seja superior a 30 indicar qual é o maior valor entre eles.

# Aqui estou solicitando os dois números para o usuário (ENTRADA)
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

# Aqui está somando os dois números (PROCESSO)
soma = num1 + num2

# Aqui está verificando se a soma é maior que 30 e qual número é o maior entre eles (CONDIÇÃO)
if (soma > 30 and num2 > num1):
    print(f"A soma é maior que 30 (o numero maior da some é de {num2})") # (SAÍDA)
elif(soma > 30 and num1 > num2):
    print(f"A soma é maior que 30 (o numero maior da some é de {num1})") # (SAÍDA)
else:
    print (f"A soma não é maior que 30") # (SAÍDA)
