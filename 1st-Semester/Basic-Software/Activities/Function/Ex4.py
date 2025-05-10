# 4) Elaborar uma função (sem retorno) que ao receber um número deve converte em Fahrenheit e exibe o resultado na tela. A fórmula de conversão é: F = (9*C+160) / 5.
def celsiusParaFahrenheit(celsius:float):
    fahrenheit = (9 * celsius + 160) / 5
    print(f"{celsius}C equivale a {fahrenheit:.2f}F")

c = float(input("Digite a temperatura em celsius: "))
celsiusParaFahrenheit(c)