# 3) Elaborar um programa que deve ler N números. Caso o usuário digite zero (0), o programa deve exibir a somatória e a média dos valores inseridos

# Lista para armazenar os números (PROCESSAMENTO)
lista = []

# Solicitaando de número (ENTRADA)
n = float(input('Digite um número: '))

# Inicialização da variável de parada (PROCESSAMENTO)
parada = 0

# Enquanto o número for diferente de zero, o programa continua a solicitar números (PROCESSAMENTO)
while  (n > parada or n < parada):
    lista.append(n)
    n = float(input('Digite um número: '))
 
# Fazendo a soma e a média dos números (PROCESSAMENTO)
soma = sum(lista)
media = soma / len(lista)

# Exibição dos resultados (SAÍDA)
print(f'A soma dos números digitas é de: {soma} \n A media é de: {media} ')