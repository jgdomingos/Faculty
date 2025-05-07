# 2) Elaborar um programa que receba quatro números inteiros, que calcule e mostre a soma e a média desses números.

# Nas 4 linhas a seguir estou solicitando ao usuário 4 números inteiros (EBTRADA)
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))
num4 = int(input("Insira o quarto número: "))

# Na primeira linha estou fazendo a soma desses 4 números e na segunda linha estou dividindo o resultado da soma por 4 (PROCESSO)
resultadoSoma = num1 + num2 + num3 + num4
resultadoMedia = resultadoSoma / 4

# E aqui estou exibindo uma mensagem com o resultado para o usuário (SAÍDA)
print(f"A soma desses quatros números é {resultadoSoma} \nE a média é {resultadoMedia}")