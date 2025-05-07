#3) Elaborar um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostra qual a classificação dessa pessoa.
# |Altura        |                Peso                        |
# |              |Até 60|Entre 60 e 90 (Inclusive)|Acima de 90|
# |Menor que 1,20|  A   |          D              |     G     |
# |De 1,20 a 1,70|  B   |          E              |     H     |
# |Maior que 1,70|  C   |          F              |     I     |

altura = int(input("Digite sua altura: (Ex: 170)")) # (ENTRADA)
peso = float(input("Digite seu peso: ")) # (ENTRADA)

if(altura < 120 and peso <= 60):
    print("Sua classificação é: A") # (SAÍDA)
elif(altura < 120 and peso >= 60 and peso <= 90):
    print("Sua classificação é: D") # (SAÍDA)
elif(altura < 120 and peso > 90):
    print("Sua classificação é: G") # (SAÍDA)

elif(altura >= 120 and altura <= 170 and peso <= 60):
    print("Sua classificação é: B") # (SAÍDA)
elif(altura >= 120 and altura <= 170 and peso >= 60 and peso <= 90):
    print("Sua classificação é: E") # (SAÍDA)
elif(altura >= 120 and altura <= 170 and peso > 90):
    print("Sua classificação é: H") # (SAÍDA)

elif(altura > 170 and peso <= 60):
    print("Sua classificação é: C") # (SAÍDA)
elif(altura > 170 and peso >= 60 and peso <= 90):
    print("Sua classificação é: F") # (SAÍDA)
elif(altura > 170 and peso > 90):
    print("Sua classificação é: I") # (SAÍDA)

else:
    print("valor invalido") # (SAÍDA)