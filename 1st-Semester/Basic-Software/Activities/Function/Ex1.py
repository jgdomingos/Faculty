# 1) Elaborar uma função (com retorno) que recebe como parâmetro um número inteiro e devolve o seu dobro.
def dobro(num:int):
    return num * 2

valor = int(input("Digite um número: "))
print(f"O dobro de {valor} é", dobro (valor))