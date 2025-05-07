# 7) Elaborar um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
# - A idade desta pessoa hoje;
# - A idade desta pessoa em 2035

# Estou solicitando o ano de nascimento e o ano atual para o usuário (ENTRADA)
nascimento = int(input("Em qual ano você nasceu? "))
anoAtual = int(input("Insira o ano atual: "))

# Aqui esta acontecendo a resolução, descobrindo a idade da pessoa e quantos anos ela terá em 2035 (PROCESSO)
idadeAtual = anoAtual - nascimento
idadeFutura = 2035 - nascimento

# Aqui estou exibindo a idade dele e a idade que ela terá em 2035 (SAÍDA)
print(f"Você tem {idadeAtual} anos e em 2035 você terá {idadeFutura} anos.")