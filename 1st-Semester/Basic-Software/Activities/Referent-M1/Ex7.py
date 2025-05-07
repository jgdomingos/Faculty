# 7) Elaborar um programa que receba três valores (A, B, C). O programa deve verificar se eles podem ser valores dos lados de um triângulo, e se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
#    • O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
#    • Chama-se equilátero o triângulo que tem três lados iguais.
#    • Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
#    • Recebe o nome de escaleno o triângulo que tem os três lados diferentes.

A = float(input("Qual o valor de A? ")) # (ENTRADA)
B = float(input("Qual o valor de B? ")) # (ENTRADA)
C = float(input("Qual o valor de C? ")) # (ENTRADA)

if (A + B < C or C + B < A or A + C < B):
    print("Esses valores NAO podem ser um triângulo") # (SAÍDA)
elif (A == B and A == C):
    print("Ele é um triângulo equilátero") # (SAÍDA)
elif (A == B or A == C or B == C):
    print("Ele é um triangulo isósceles") # (SAÍDA)
elif (A != B != C):
    print("Ele é um triangulo escaleno") # (SAÍDA)