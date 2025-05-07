# 18) Elaborar um programa que leia o tempo de duração de um evento em uma fábrica expressa em segundos e mostre-o expresso em horas, minutos e segundos.

# Aqui estou solicitando o tempo de duração do eventos em segundos (ENTRADA)
duracao = int(input("Qual foi o tempo de duração do evento (Insira em segundos)? "))

# Nas 3 linhas a seguir está fazendo a conversão para Horas, Minutos e Segundos (PROCESSO)
horas = duracao // 3600
minutos = (duracao % 3600) // 60
segundos = duracao % 60

# Aqui estou mostrando o resultado em tempo total para o usuário (SAÍDA)
print(f"O eventos teve uma duração de {horas}:{minutos}:{segundos}")