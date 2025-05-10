# 6) Elaborar uma função (sem retorno) que recebe dois valores inteiros passados como parâmetro. Logo em seguida a função deve exibir um menu com 4 opções (cada opção levará para uma função com retorno diferente):
# a) Soma
# b) Subtrair
# c) Multiplicar
# d) Dividir
# e) Raiz quadrada do primeiro número.
# Quando o usuário selecionar a operação desejada, a função correspondente deve exibir o resultado na tela.
import math

def soma(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def raizQuadrada(a):
    return math.sqrt(a)

def calculadora(a, b):
    print("Escolha uma opção abaixo:" \
          "\n1- Soma" \
          "\n2- Subtrair" \
          "\n3- Multiplicar" \
          "\n4- Dividir" \
          "\n5- Raiz Quadrada")
    
    opcao = int(input("Digite o número da opção: "))

    if (opcao == 1):
        print(f"A soma é {soma(a, b)}")
    elif (opcao == 2):
        print(f"A subtração é {subtrair(a, b)}")
    elif (opcao == 3):
        print(f"A multiplicação é {multiplicar(a, b)}")
    elif (opcao == 4):
        print(f"A divisão é {dividir(a, b)}")
    elif (opcao == 5):
        print(f"A raiz quadrada de {a} é {raizQuadrada(a):.2f}")
    else:
        print("Opção inválida")

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo valor: "))
calculadora (x, y)