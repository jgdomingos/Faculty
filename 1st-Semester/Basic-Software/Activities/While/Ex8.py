# 8) Elaborar um programa que contem uma lista com N elementos. Essa lista deve ser preenchidapelo usuário e só deve conter números inteiros positivos e pares. Caso o usuário digite o número 1 a repetição termina. Exibir no final todos os elementos da lista

# Lista para armazenar os números (PROCESSAMENTO)
listaNum=[]

# Solicitando número (ENTRADA)
numero=int(input('Digite um número aleatório:\n'))

# Verificando se o número é par e positivo (PROCESSAMENTO)
# Enquanto o número for diferente de 1, o programa continua a solicitar números (PROCESSAMENTO)
while (numero != 1):
    if (numero % 2 == 0 and numero > 0):
        listaNum.append(numero)
        
    numero=int(input('Digite outro número:\n'))

# Exibição dos resultados (SAÍDA)
print(f'Números pares e positivos: {listaNum}')