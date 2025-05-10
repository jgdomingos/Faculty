# 3) Elaborar uma função que retorna o cálculo do volume de uma esfera. Sendo que o raio é passado por parâmetro.
import math

def volumeEsfera(raio:float):
    return (4/3) * math.pi * raio ** 3

raio = float(input("Digite o valor do raio: "))
print(f"O volume da esfera {raio} é, {volumeEsfera(raio):.2f}")