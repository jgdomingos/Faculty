# 11) Elaborar um programa que calcule a aceleração de um corpo em movimento conhecendo-se as velocidades inicial e final, e o intervalo de tempo medido (a = (v2 –v1)/∆t). Exibir o resultado

# Nas 3 linhas a seguir estou solicitando ao usuário valocidade inicial, final e o intervalo de tempo (ENTRADA)
velocidadeInicial = float(input("Qual é a velocidade inicial? "))
velocidadeFinal = float(input("Qual é a velocidade final? "))
intervaloTempo = float(input("Qual o intervalo de tempo medido? "))

# Aqui está calculando a aceleração do corpo em movimento (PROCESSO)
aceleracao = (velocidadeFinal - velocidadeInicial) / intervaloTempo

# Aqui estou mostrando o resultado para o usuário (SAÍDA)
print(f"A aceleração desse corpo em movimento é de {aceleracao}")