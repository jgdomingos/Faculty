# 5) Elaborar um programa que lê um número N inteiro maior que 2 (caso N não for maior que 2 deve solicitar outro número). Logo após o programa deve exibir o quadrado e o cubo de 2 até N

# Estou importando a biblioteca math para usar a função pow
import math

# Solicitando de número (ENTRADA)
numero=int(input('Digite um número acima de 2:\n'))

# Enquanto o número for menor que 2, o programa continua a solicitar números (PROCESSAMENTO)
while (numero < 2):
    print('número inválido, tente novamente...')

    numero=int(input('Digite um número acima de 2:\n'))

# Inicializando as variáveis quadrado e cubo (PROCESSAMENTO)
for i in range(2,numero +1):
    quadrado=math.pow(numero, 2)
    cubo=math.pow(numero, 3)

# Exibição dos resultados (SAÍDA)
print(f'O número é {numero}\nAo quadrado é: {quadrado:.2f}\nAo cubo é: {cubo:.2f}')