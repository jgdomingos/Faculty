# 6) Elaborar um programa que solicita um número (entre 10 a 15). Se o usuário digitar um número diferente, o programa deve mostrar a mensagem “Entrada inválida” e solicitar um número novamente. Se digitar correto o programa deve mostrar a raiz quadrada desse número e termina

# Estou importando a biblioteca math para usar a função sqrt
import math

# Solicitando o número (ENTRADA)
num = int(input('Digite um número entre 10 e 15: '))

# Enquanto o número estiver fora do intervalo de 10 a 15, o programa continua a solicitar números (PROCESSAMENTO)
while num < 10 or num > 15:
    print('Entrada inválida')
    num = int(input('Digite um número entre 10 e 15: '))

# Exibição da raiz quadrada do número (SAÍDA)
print(f'A raiz quadrada de {num} é {math.sqrt(num):.2f}')