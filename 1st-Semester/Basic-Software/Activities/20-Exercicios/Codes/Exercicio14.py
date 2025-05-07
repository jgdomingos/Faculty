# 14) Elaborar um programa que leia uma temperatura em graus Celsius e deve converter em graus Fahrenheit. A fórmula de conversão é: F = (9*C+160)/5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius. Exibir a temperatura em Fahrenheit.

# Estou solicitando ao usuário a temperatura atual em graus celsius (ENTRADA)
grausCelsius = int(input("Qual a temperatura atual? "))

# Aqui está acontecendo a conversão para Fahrenheit (PROCESSO)
fahrenheit = (9 * grausCelsius + 160) / 5

# Aqui estou mostrando a conversão para o usuário (SAÍDA)
print(f"A tempetatura {grausCelsius}ºC em Fahrenheit é {fahrenheit}ºF")