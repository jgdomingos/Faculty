# 13) Elaborar um programa que receba o raio e a altura de uma lata de óleo para calcular e apresentar o valor do volume desta lata, dado: V = π*r2*h.

# Estou importando cálculos matemáticos
import math

# Nas duas linhas a seguir estou solicitando ao usuário o raio e a altura da lata de óleo (ENTRADA)
raio = float(input("Qual é o raio da lata de óleo? "))
altura = float(input("Qual a altura dessa lata de óleo? "))

# Aqui está calculando o volume da lata de óleo (PROCESSO)
volume = math.pi * math.pow(raio, 2) * altura

# Aqui estou mostrando o resultado para o usuário (SAÍDA)
print(f"O volume dessa lata de óleo é {volume}")