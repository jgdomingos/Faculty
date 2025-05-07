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