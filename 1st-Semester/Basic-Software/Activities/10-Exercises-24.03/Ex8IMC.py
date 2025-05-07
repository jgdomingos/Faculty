# 8) O IMC - Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar Uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC = peso (altura)**2. Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo com a tabela abaixo.

# Aqui estou solicitando ao usuário o peso e altura (ENTRADA)
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

# Aqui está calculando (PROCESSO)
imc = peso / (altura)**2

# Aqui está verificando o peso da pessoa (CONDIÇÃO)
if( imc < 18.5):
    print(f"Abaixo do peso! {imc}") # (SAÍDA)
elif(imc >= 18.5 and imc <= 25):
    print(f"Peso normal {imc}") # (SAÍDA)
elif(imc >= 25 and imc <= 30):
    print(f"Acima do peso! {imc}") # (SAÍDA)
elif(imc > 30):
    print(f"Obeso!!! ({imc})") # (SAÍDA)