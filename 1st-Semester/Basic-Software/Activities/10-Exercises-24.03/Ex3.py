# 3) Elaborar um algoritmo que deve receber um número qualquer e exibir se é par ou ímpar

# Aqui estou solicitando para o usuário o número (ENTRADA)
num1 = int(input("Digite um numero: "))

# Aqui está tendo um processo para verificar se o número é par ou ímpar (PROCESSO)
if (num1 % 2 == 0 ):
    print(f"O numero {num1} é par!") # (SAÍDA)
else: 
    print(f"O numero {num1} é impar!") # (SAÍDA)