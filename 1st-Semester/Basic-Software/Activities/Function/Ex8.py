# 8) Elaborar uma função (sem retorno) que imprime todos os números primos de 2 a N (essa função deve utilizar a função do exercício 7). Sendo que N é um número inserido pelo usuário, que deve ser superior a 2 (solicitar um novo número caso o usuário digite um número menor ou igual a 2).
def primo(num:int):
    if (num < 2):
        return 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 0
    return 1

def imprimirPrimos(n:int):
    print(f"Números primos de 2 até {n}:")
    for i in range(2, n+1):
        if primo(i):
            print(i, end=" ")

while True:
    n = int(input("Digite um número maior que 2: "))
    if (n > 2):
        break
    print("Número inválido")

imprimirPrimos(n)