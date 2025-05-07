# 5) Elaborar um algoritmo que solicita ao usuário para digitar 15 valores e deve exibir a soma e média.
 
dados = []
 
for rep5 in range(1,16):
    numero = float(input("Qual o número? "))
    valores = dados.append(numero)
 
soma = sum(dados)
media = soma / 15
print(f"A soma desses número é {soma} e a média é {media}")