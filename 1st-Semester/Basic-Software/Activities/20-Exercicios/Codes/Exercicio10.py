# 10) Elaborar um programa que dados dois lados de um triângulo retângulo calcule e exiba a respectiva hipotenusa

# Estou importando cálculos matemáticos
import math

# Nas duas linhas a seguir estou solicitando ao usuário o tamanho de dois lados desse Triângulo Retângulo. O HYPOT calcula o comprimento da hipotenusa de um triângulo retângulo(ENTRADA)
ladoA = float(input("Digite o tamanho do lado A: "))
ladoB = float(input("Digite o tamanho do lado B: "))

# Aqui está calculando a Hipotenusa (PROCESSO)
hipotenusa = math.hypot(ladoA, ladoB)

# Aqui estou mostrando o resultado para o usuário (SAÍDA)
print(f"A Hipotenusa desse triângulo retângulo é {hipotenusa}")