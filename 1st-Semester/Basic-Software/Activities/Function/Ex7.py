# 7) Elaborar uma função (com retorno) que determina se um número passado como parâmetro é primo. A função quando chamada retorna 1 indicando que o número é primo e 0 caso contrário.
def primo(num:int):
    if (num < 2):
        return 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 0
    return 1

numero = int(input("Digite um número: "))
if primo(numero):
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo")