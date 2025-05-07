# 9) Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal da etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
# 1) A vista em dinheiro ou em cheque
# 2) A vista no cartão de crédito 
# 3) Em duas vezes 
# 4) Em mais de duas vezes

# Aqui estou solicitando o valor do produto e a forma de pagamento (ENTRADA)
valor = float(input("Digite o valor do produto: "))
pagamento = int(input("Digite a forma de pagamento: (1 = A vista em dinheiro ou em cheque | 2 = A vista no cartão de crédito | 3 = Em duas vezes | 4 = Em mais de duas vezes): "))

# Aqui está verificando a forma de pagamento escolhido e o valor que terá que pagar (CONDIÇÃO)
if (pagamento == 1):
    desconto = valor * 0.10 
    pagar = valor - desconto
    print(f"Você recebeu 10 por cento de desconto! O valor da compra é de {pagar}") # (SAÍDA)
elif (pagamento == 2):
    desconto = valor * 0.15 
    pagar = valor - desconto
    print(f"Você recebeu 15 por cento de desconto! O valor da compra é de {pagar}") # (SAÍDA)
elif (pagamento == 3):
    pagar = valor / 2
    print(f"você pagara em duas vezes de {pagar}") # (SAÍDA)
elif (pagamento == 4):
    juros = valor * 0.10
    pagar = valor + juros
    print(f"Você recebeu 10 por cento de juros! O valor da compra é de {pagar}") # (SAÍDA) 
else:
    print("Escolha uma forma de pagamento valida!") # (SAÍDA)