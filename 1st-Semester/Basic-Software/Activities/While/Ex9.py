#9) Elaborar um programa que contenha uma lista com 25 elementos em que o usuário deve preencher com valores reais. Logo em seguida, deve ser solicitado ao usuário que digite dois números. Esses números devem corresponder a posições na lista (caso contrário solicite um novo valor). Após inserir os dois números o programa deve exibir a soma dos elementos das duas posições da lista.


numeros = []

print('Digite 25 valores reais.')

while len(numeros) < 25:
    numero = float(input(f'Valor {len(numeros)+1}: '))
    numeros.append(numero)

# Solicita a primeira posição (1 a 25) e converte para índice (0 a 24)
position1 = int(input('Digite uma posição (1 até 25): '))
while position1 < 1 or position1 > 25:
    print('Posição inválida, tente novamente')
    position1 = int(input('Digite uma posição (1 até 25): '))

# Solicita a segunda posição (1 a 25) e converte para índice (0 a 24)
position2 = int(input('Digite outra posição (1 até 25): '))
while position2 < 1 or position2 > 25:
    print('Posição inválida, tente novamente')
    posicao02 = int(input('Digite outra posição (1 até 25): '))

# Converte para índices de lista (subtrai 1)
i1 = position1 - 1
i2 = position2 - 1

soma = numeros[i1] + numeros[i2]

print(f"Soma dos elementos nas posições {position1} e {position2}: {soma:.2f}")