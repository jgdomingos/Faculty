#1) Elaborar um programa que leia a idade e o tempo de serviço de um trabalhador e mostre se o trabalhador pode ou não se aposentar. As condições para aposentadoria são:
#    • Ter pelo menos 65 anos,
#    • Ou ter trabalhado pelo menos 30 anos,
#    • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade = int(input("Digite sua idade?: ")) # (ENTRADA)
tempoServico = int(input("Qual seu tempo de serviço?: ")) # (ENTRADA)

if(idade >= 65 or tempoServico >= 30):
    print("Você ja pode se aposentar!")
elif (idade >= 60 and tempoServico >= 25):
    print("Você ja pode se aposentar!")
else:
  print ("Você não pode se aposentar!") # (SAÍDA)


#2) Elaborar um programa que leia a distancia em km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o consumo em Km/l e mostre uma mensagem de acordo com a tabela abaixo:
# |CONSUMO  |(Km/l)|   MENSAGEM    |
# |Menor que|  8   | Venda o carro!|
# |Entre    |8 e 14|   Econômico   |
# |Maior que|  14  |Super econômico|

km = float(input("Digite a distância percorrida: (KM)")) # (ENTRADA)
gasolina = float(input("Digite o consumo de gasolina utilizado: ")) # (ENTRADA)

kml = km / gasolina

if(kml <8):
    print ("Venda o carro!") # (SAÍDA)
elif(kml >= 8 and kml <14):
    print("Econmico!") # (SAÍDA)
else:
    print("Super Econômico!") # (SAÍDA)


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


#4) Um produto vai sofrer aumento de acordo com a tabela abaixo. Elaborar um programa que leia o preço antigo, calcule e mostre o preço novo, e mostre uma mensagem em função do preço novo (de acordo com a segunda tabela)
# |PREÇO ANTIGO    |PERCENTUAL DE AUMENTO|    |PREÇO NOVO                     |MENSAGEM  |
# |Até R$50        |         5%          |    |Até R$80                       |Barato    |
# |Até R$50 e R$100|        10%          |    |Entre R$80 e R$120 (inclusive) |Normal    |
# |Acima de R100   |        15%          |    |Entre R$120 e R$200 (inclusive)|Caro      |
#                                             |Acima de R$200                 |Muito caro|

precoAntigo = float(input("Digite o valor antigo: ")) # (ENTRADA)

if (precoAntigo <= 50):
    precoNovo = precoAntigo + (precoAntigo * 0.05)
elif (precoAntigo > 50 and precoAntigo <= 100):
    precoNovo = precoAntigo + (precoAntigo * 0.10)
else:
    precoNovo = precoAntigo + (precoAntigo * 0.15)

if (precoNovo <= 80):
    print (f"Preço novo:{precoNovo}\n Barato") # (SAÍDA)
elif (precoNovo > 80 and precoNovo <= 120):
    print (f"Preço novo:{precoNovo}\n Normal") # (SAÍDA)
elif (precoNovo > 120 and precoNovo <= 200):
    print(f"Preço novo:{precoNovo}\n Caro") # (SAÍDA)
else:
    print(f"Preço novo:{precoNovo}\n Muito caro") # (SAÍDA)


# 5) Elaborar um programa para automatizar o caixa de uma lanchonete. Este algoritmo deve ler o código do item pedido, a quantidade e calcular o valor a ser pago por aquele lanche. No final o programa deve mostrar o total a ser pago. O cardápio da lanchonete é o seguinte:
# |Código|   Especificação   |Preço Unitário (R$)|
# |  100 |  Cachorro Quente  |       3,50        |
# |  101 |   Bauro Simples   |       3,80        |
# |  102 |    Bauro c/ovo    |       4,50        |
# |  103 |     Hamburger     |       4,70        |
# |  104 |   Cheeseburger    |       5,30        |
# |  105 |   Refrigerante    |       4,00        |

codigo = int(input("\n100 - Cachorro Quente | R$3,50"
"\n101 - Bauru Simples | R$3,80"
"\n102 - Bauru c/ovo | R$4,50"
"\n103 - Hamburger | R$4,70"
"\n104 - cheseeburger | R$5,30"
"\n105 - Refrigerante | R$4,00\n\n"
"Qual o código do lanche/bebida que deseja pedir?")) # (ENTRADA)
quantidade = int(input("Qual a quantidade que desaja consumir: ")) # (ENTRADA)

if(codigo == 100):
    pagar = 3.50
elif(codigo == 101):
    pagar = 3.80
elif(codigo == 102):
    pagar = 4.50
elif(codigo == 103):
    pagar = 4.70
elif(codigo == 104):
    pagar = 5.30
elif(codigo == 105):
    pagar = 4.00
else:
    print("Valor inválido") # (SAÍDA)

totalPagar = pagar * quantidade
print(f"O valor final do pedido é de R${totalPagar}") # (SAÍDA)


# 6) Elaborar um programa que mostre ao usuário um menu com 4 opções de operações matemáticas (1- soma, 2- subtração, 3- multiplicação e 4- divisão). Após o usuário escolher uma das opções, o programa deve solicitar dois números e realiza a operação escolhida. Logo em seguida, o programa deve mostrar qual foi conta realizada e qual o resultado.

operacao= int(input("\n1 - Soma"
"\n2 - Subtração"
"\n3 - Multiplicação"
"\n4 - Divisão\n\n"
"Qual operção matemática deseja realizar? ")) # (ENTRADA)

num1 = float(input("Digite um número: ")) # (ENTRADA)
num2 = float(input("Digite outro número: ")) # (ENTRADA)

if(operacao == 1):
    resultado = num1 + num2
elif(operacao == 2):
    resultado = num1 - num2
elif(operacao == 3):
    resultado = num1 * num2
elif(operacao == 4):
    resultado = num1 / num2
else:
    print("Valor inválido")

print(f"O resultado dessa operação matemática é {resultado}") # (SAÍDA)


# 7) Elaborar um programa que receba três valores (A, B, C). O programa deve verificar se eles podem ser valores dos lados de um triângulo, e se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
#    • O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
#    • Chama-se equilátero o triângulo que tem três lados iguais.
#    • Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
#    • Recebe o nome de escaleno o triângulo que tem os três lados diferentes.

A = float(input("Qual o valor de A? ")) # (ENTRADA)
B = float(input("Qual o valor de B? ")) # (ENTRADA)
C = float(input("Qual o valor de C? ")) # (ENTRADA)

if (A + B < C or C + B < A or A + C < B):
    print("Esses valores NAO podem ser um triângulo") # (SAÍDA)
elif (A == B and A == C):
    print("Ele é um triângulo equilátero") # (SAÍDA)
elif (A == B or A == C or B == C):
    print("Ele é um triangulo isósceles") # (SAÍDA)
elif (A != B != C):
    print("Ele é um triangulo escaleno") # (SAÍDA)


# 8) Elaborar um programa que leia três números inteiros positivos e efetue o cálculo de uma das seguintes médias de acordo a letra digitada pelo usuário:

import math
menu = (input("\na - Geométrica"
"\nb - Ponderada"
"\nc - Harmônica"
"\nd - Aritmética\n\n"
"Qual operção matemática deseja realizar? ")) # (ENTRADA)

num1 = int(input("Insira o primeiro número, ele deve ser inteiro e positivo: ")) # (ENTRADA)
num2 = int(input("Insira o segundo número, ele deve ser inteiro e positivo: ")) # (ENTRADA)
num3 = int(input("Insira o terceiro número, ele deve ser inteiro e positivo: ")) # (ENTRADA)

if (menu == "a"):
    mult = num1 * num2 * num3
    resultado = pow(mult, 1/3)
    print(f"O resultado dessa operação é {resultado}") # (SAÍDA)
elif (menu == "b"):
    resultado = (num1 + 2 * num2 + 3 * num3) / 6
    print(f"O resultado dessa operação é {resultado}") # (SAÍDA)
elif (menu == "c"):
    resultado = ((1 / num1) + (1 / num2) + (1 / num3)) / 1
    print(f"O resultado dessa operação é {resultado}") # (SAÍDA)
elif (menu == "d"):
    resultado = (num1 + num2 + num3) / 3
    print(f"O resultado dessa operação é {resultado}") # (SAÍDA)
else:
    print("Opção inválida") # (SAÍDA)