# 12) Elaborar um programa que receba o raio de uma esfera. O algoritmo deve calcular e exibir a área e o volume da esfera

# Estou importando cálculos matemáticos
import math

# Estou solicitando ao usuário o valor do Raio da esfera (ENTRADA)
raio = float(input("Qual é o raio dessa esfera? "))

# Nas duas linhas a seguir está calculando o volume e a área dessa esfera (PROCESSO)
volume = (4 / 3) * math.pi * math.pow(raio, 3)
area = 4 * math.pi * math.pow(raio, 2)

# Aqui estou mostrando o resultado para o usuário (SAÍDA)
print(f"O volume dessa esfera é: {volume}\nA área dessa esfera é {area}")