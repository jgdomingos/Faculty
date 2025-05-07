# 10) Elaborar um programa que contem uma lista com 15 elementos. Essa lista deve ser preenchidapelo usuário, porém não deve conter valores repetidos. Exibir no final a lista

lista = []

while len(lista) < 15:
    num = int(input(f'Digite um número inteiro ({len(lista) + 1}/15): '))
    if num not in lista:
        lista.append(num)
    else:
        print('Número repetido! Digite outro.')

print('Lista final:', lista)