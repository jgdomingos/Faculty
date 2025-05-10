# 5) Elaborar uma função (com retorno) que ao receber um número deve converte em Kelvin e exibe o resultado na tela. A fórmula de conversão é: K=C+273.15.
def celsiusParaKelvin(celsius:float):
    return celsius + 273.15

c = float(input("Digite a temperatura em celsius: "))
print(f"{c}C equivale a {celsiusParaKelvin(c):.2f}K")