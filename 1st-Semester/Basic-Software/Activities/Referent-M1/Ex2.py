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