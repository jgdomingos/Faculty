# 2) Elaborar uma função (com retorno) que verifica se um número é positivo ou negativo. Sendo que o valor de retorno será 1 se positivo, -1 se negativo e 0 se for igual a 0
def verificarNum(num:float):
    if (num > 0):
        return 1
    elif (num < 0):
        return -1
    else:
        return 0
    
valor2 = int(input("Digite um número: "))
print(f"O {valor2} é", verificarNum (valor2))