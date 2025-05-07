# 4) Elabore um algoritmo que lê um número inteiro entre 1 e 7 e exibe o dia da semana correspondente. Caso o usuário digite um número fora desse intervalo, o algoritmo mostra uma mensagem informando "Número inválido"

# Aqui estou solicitando para o usuário o número (ENTRADA)
num = int(input("Digite um numero de 1 a 7: "))

# Nas linhas a seguir está verificando qual o dia da semana é correspondente ao número digitado, ou se é um número inválido (CONDIÇÃO)
if (num == 1):
    print("Domingo.") # (SAÍDA)

elif (num == 2):
    print("Segunda.") # (SAÍDA)

elif (num == 3):
    print("Terça.") # (SAÍDA)

elif (num == 4):
    print("Quarta.") # (SAÍDA)

elif (num == 5):
    print("Quinta.") # (SAÍDA)

elif (num == 6):
    print("Sexta.") # (SAÍDA)

elif (num == 7):
    print("Sabado.") # (SAÍDA)

else:
    print("O numero digitado é invalido") # (SAÍDA)
