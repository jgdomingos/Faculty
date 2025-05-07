# 16) Elaborar um programa que leia 3 notas de um aluno e calcule a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é: 2, 3 e 5, respectivamente.

# Estou solicitando ao usuário as 3 notas que o aluno tirou (ENTRADA)
nota1 = float(input("Qual foi a primeira nota? "))
nota2 = float(input("Qual foi a segunda nota? "))
nota3 = float(input("Qual foi a terceira nota? "))

# Estou indicando ao sistema o peso de cada nota
peso1 = 2
peso2 = 3
peso3 = 5

# Aqui está calculando a média final do aluno (PROCESSO)
media = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3) / peso1 + peso2 + peso3

# Aqui estou mostrando o resultado a média final para o usuário (SAÍDA)
print(f"A média final desse aluno é {media:.2f}")