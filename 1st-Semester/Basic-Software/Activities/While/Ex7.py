# Nas 3 linhas a seguir estou informando ao sistema os dados
pedido = [0,1,2,3,4] # 0 - Nome do cliente, 1 - Nome do pedido, 2 - Preço, 3 - Quantidade, 4 - Valor total
esp = ["Hot-Dog","X-Burger","X-Egg","X-Tudo","Refrigerante","Água"] # Cardápio
preco = [20,28,32,40,8,5] # Preço dos produtos

novoPedido = input("Novo Pedido? (S/N) ") # Pergunta se o cliente quer fazer um novo pedido

# Se o cliente responder "S" ou "s" o sistema continua, caso contrário ele cancela o pedido
while (novoPedido == "S" or novoPedido == "s"):
  pedido[0] = input("Digite o nome do cliente: ") # Aqui o cliente informa o nome dele
  pedido[4] = 0 # Aqui o sistema inicializa o valor total do pedido como 0

  while True:
    # Aqui o sistema imprime o cardápio e pede para o cliente escolher o que ele quer
    print("\nCódigo |  Cardápio  | Preço\n" \
    "1   -   Hot-Dog       - R$20,00\n" \
    "2   -   X-Burguer     - R$28,00\n" \
    "3   -   X-Egg         - R$32,00\n" \
    "4   -   X-Tudo        - R$40,00\n" \
    "5   -   Refrigerante  - R$8,00\n" \
    "6   -   Água          - R$5,00\n")

    # Aqui o cliente escolhe o que ele quer e informa a quantidade
    cod = int(input("Escolha o código do seu pedido: "))
    if cod == 0:
      print("Pedido cancelado!") # Aqui o sistema imprime que o pedido foi cancelado, caso o cliente não queira fazer um novo pedido
      break # Aqui o sistema encerra o loop e cancela o pedido

    cod = cod - 1 # Aqui o código do pedido é ajustado para começar em 0, já que a lista começa em 0 e o cliente escolhe de 1 a 6

    # Aqui o sistema verifica se o código do pedido é válido, ou seja, se está entre 0 e 5 (já que a lista tem 6 elementos)
    # Se o código for válido, o sistema pede a quantidade e calcula o valor total do pedido
    if(cod >= 0 and cod < 6):
        qnd = int(input("Insira a quantidade: ")) # Aqui o cliente informa a quantidade do pedido
 
        nome = esp[cod] # Aqui o sistema pega o nome do pedido, que está na lista esp, de acordo com o código que o cliente escolheu
        valor = preco[cod] # Aqui o sistema pega o preço do pedido, que está na lista preco, de acordo com o código que o cliente escolheu
        valorTotal = valor * qnd # Aqui o sistema calcula o valor total do pedido, multiplicando o preço pela quantidade

        # Aqui o sistema armazena os dados do pedido na lista pedido, que foi criada no início do código
        pedido[1] = nome # Aqui o sistema armazena o nome do pedido na lista pedido
        pedido[2] = valor # Aqui o sistema armazena o preço do pedido na lista pedido
        pedido[3] = qnd # Aqui o sistema armazena a quantidade do pedido na lista pedido
        pedido[4] = valorTotal # Aqui o sistema armazena o valor total do pedido na lista pedido

        # Aqui o sistema imprime os dados do pedido, que foram armazenados na lista pedido
        print(f"Cliente: {pedido[0]}") # Aqui o sistema imprime o nome do cliente
        print(f"Pedido: {pedido[1]}") # Aqui o sistema imprime o pedido
        print(f"Valor: R${pedido[2]}") # Aqui o sistema imprime o preço do pedido
        print(f"Quantidade: {pedido[3]}") # Aqui o sistema imprime a quantidade do pedido
        print(f"Valor à pagar: R${pedido[4]}") # Aqui o sistema imprime o valor total do pedido

    else:
        print("Codigo invalido") # Aqui o sistema imprime que o código do pedido é inválido, ou seja, não está entre 0 e 5

    # Aqui o sistema pergunta se o cliente quer confirmar o pedido ou não
    # Se o cliente responder "S" ou "s", o sistema finaliza o pedido, caso contrário ele cancela o pedido
    confirma = input("Confirmar pedido? (S/N) ")

    # Aqui o sistema verifica se o cliente quer confirmar o pedido ou não
    if(confirma == "S" or confirma == "s"):
      print("Pedido Finalizado!") # Aqui o sistema imprime que o pedido foi finalizado
    else: 
      print("Pedido Cancelado!") # Aqui o sistema imprime que o pedido foi cancelado
 
else:
  print("Pedido cancelado!") # Aqui o sistema imprime que o pedido foi cancelado, caso o cliente não queira fazer um novo pedido