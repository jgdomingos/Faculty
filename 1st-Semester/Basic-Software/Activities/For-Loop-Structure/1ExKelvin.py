# 1) Elaborar um algoritmo que leia um valor de temperatura em graus Celsius, calcule e exiba a temperatura equivalente em Kelvin, sabendo que: K = C + 273. Esse algoritmo deve repetir 5 vezes
 
for rep in range(1,6):
    celsius = int(input("Qual a temperatura em Censius? "))
    K = celsius + 273
    print(K)