# 4) Elaborar um programa que solicite ao usuário vários valores inteiros. Quando o usuário digitar o número 100 o programa deve terminar, mostrando quantos valores foram acima de 80, quantos foram abaixo de 10 e mostrar a média de todos os valores digitados pelo usuário

# Lista para armazenar os números (PROCESSAMENTO)
lista = []
lista80 = []
lista10 = []

# Solicitaando de número (ENTRADA)
num = int(input('Digite um número: '))
 
# Processo para identificar os números (PROCESSAMENTO)
# Enquanto o número for diferente de 100, o programa continua a solicitar números (PROCESSAMENTO)
while (num != 100):
    if (num >= 80):
        lista80.append(num)
        num = int(input('Digite um número: '))
    elif (num <= 10):
        lista10.append(num)
        num = int(input('Digite um número: '))
    else:
        lista.append(num)
        num = int(input('Digite um número: '))

# Fazendo a soma e a média dos números (PROCESSAMENTO)
soma = sum(lista) + sum(lista80) + sum(lista10)
media = soma / (len(lista) + len(lista80) + len(lista10))

# Exibição dos resultados (SAÍDA)
qnt80 = len(lista80)
qnt10 = len(lista10)

# Exibição dos resultados (SAÍDA)
print(f'A soma dos números é {soma}\nA média é {media}\nTem {qnt80} maior que 80 e {qnt10} menor que 10')