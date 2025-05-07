# 1) Elabore um algoritimo que receba dois números e apresente-os em ordem crescente

# Aqui estou solicitando os dois números para o usuário (ENTRADA)
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

# Aqui está tendo um processo para verificar a ordemc rescente (PROCESSO)
if (num1 > num2):
    print (f"a ordem crescente é: {num2}, {num1}") # (saída)
else: 
    print (f"a ordem crescente é: {num1},{num2}") # (SAÍDA)
     