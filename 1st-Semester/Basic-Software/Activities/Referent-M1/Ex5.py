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