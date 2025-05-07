# 1) Elaborar um programa que solicita varias temperaturas em graus Celsius. Para cada temperatura inserida, o programa deve converter para graus Fahrenheit e Kelvin e mostrar na tela. O programa termina quanto a temperatura inserida for menor que -5.

# Solicitando de temperatura em Celsius (ENTRADA)
celsius = float(input('Digite a Temperatura em Celsius:  '))

# Enquanto a temperatura for maior que -5, o programa continua a solicitar temperaturas
# e realizar as conversões (PROCESSAMENTO)
while (celsius > -5):
   
    # Conversão de Celsius para Fahrenheit e Kelvin (PROCESSAMENTO)
    f = (9*celsius + 160) / 5
    k = celsius + 273

    # Exibição dos resultados (SAÍDA)
    print(f'Celsius = {celsius}° | Kelvin = {k}° | Fahrenheit = {f}°')
   
    # Solicitando de nova temperatura em Celsius (ENTRADA)
    celsius = float(input('Digite a Temperatura em Celsius:  '))

# Mensagem de encerramento do programa (SAÍDA)
print('Programa encerrado')