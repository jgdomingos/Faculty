# 2) Elaborar um programa que lê um número inteiro entre 1 e 7 e exibe o dia da semana correspondente. O programa deve repetir até que o usuário digite um número fora desse intervalo, caso isso aconteça o algoritmo mostra uma mensagem informando “Número inválido”

# Solicitando de número entre 1 e 7 (ENTRADA)
dia = int(input('Digite um numero de 1 à 7: '))

# Enquanto o número estiver entre 1 e 7, o programa continua a solicitar números e exibir os dias da semana correspondentes (PROCESSAMENTO)
while(dia < 8 and dia > 0):
    if(dia == 1):
        print("Domingo")
        dia = int(input('Digite um numero de 1 à 7: '))
    elif(dia == 2):
        print('Segunda')
        dia = int(input('Digite um numero de 1 à 7: '))
    elif(dia == 3):
        print('Terça')
        dia = int(input('Digite um numero de 1 à 7: '))
    elif(dia == 4):
        print('Quarta')
        dia = int(input('Digite um numero de 1 à 7: '))
    elif(dia == 5):
        print('Quinta')
        dia = int(input('Digite um numero de 1 à 7: '))
    elif(dia == 6):
        print('Sexta')
        dia = int(input('Digite um numero de 1 à 7: '))
    else:
        print('Sabado')
        dia = int(input('Digite um numero de 1 à 7: '))
   
# Mensagem de encerramento do programa (SAÍDA)
print('Numero invalido')