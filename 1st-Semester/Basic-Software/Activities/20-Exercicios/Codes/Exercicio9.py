# ) Elaborar um programa que receba um número positivo e maior que zero, calcule e mostre:
# a) o número digitado ao quadrado;
# b) a raiz quadrada do número digitado;

# Estou importando cálculos matemáticos
import math

# Estou solicitando ao usuário um número positivo e maior que zero (ENTRADA)
numero = int(input("Insira um número positivo e maior que zero: "))

# Nas duas linhas a seguir está calculado o quadrado e a raiz quadrada desse número (PROCESSO)
aoQuadrado = numero * numero
raiz = math.sqrt(numero)

# Aqui estou mostrando o resultado para o usuário (SAÍDA)
print(f"O quadrado desse número é: {aoQuadrado}\nE a raiz quadrada desse número é: {raiz}")