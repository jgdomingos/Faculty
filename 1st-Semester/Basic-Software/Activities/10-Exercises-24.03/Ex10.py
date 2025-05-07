# 10) Escreva um algoritmo que leia o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação, e calcule a média de aproveitamento, usando a fórmula MA = (nota1 + nota2 * 2 + nota3 * 3 + ME) / 7

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
me = float(input("Digite a média dos exercícios: "))

ma = (nota1 + nota2 * 2 + nota3 * 3 + me) / 7

print(f"A média de aproveitamento é: {ma:.2f}")