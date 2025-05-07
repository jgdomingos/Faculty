# 20) Elaborar um programa que receba o número de horas trabalhadas e o valor do salário mínimo. Calcule e mostre o salário a receber seguindo as regras abaixo:
# a) o valor da hora trabalhada vale a metade do salário mínimo;
# b) o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada;
# c) o imposto equivale a 3% do salário bruto;
# d) o salário a receber equivale ao salário bruto menos o imposto.

# Aqui estou solicitando ao usuário quantas horas ele trabalhou e o valor do salário mínimo (ENTRADA)
horasTrabalhadas = int(input("Quantas horas você trabalhou? "))
salarioMinimo = float(input("Qual o valor do salário mínimo? "))

# Aqui está calculando todo o valor que o usuário deve receber (PROCESSO)
valorHoraTrabalhada = salarioMinimo / 2
salarioBruto = horasTrabalhadas * valorHoraTrabalhada
imposto = salarioBruto * 0.03
salario = salarioBruto - imposto

# Aqui está mostrando o salário que ele deve recber (SAÍDA)
print(f"Você deve receber {salario}")