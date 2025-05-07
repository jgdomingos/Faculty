# 4) Elaborar um programa que calcule o consumo médio de um automóvel (medido em km/l), dado que são conhecidos a distância total percorrida e o volume de combustível consumido para percorrê-la (medido em litros).

# Nas duas linhas a seguir estou solicitando ao usuário quantos KMs ele rodou e qual foi o consumo de combustível (ENTRADA)
distanciaPercorrida = float(input("Insira quantos Km você rodou: "))
combustivelConsumido = float(input("Insira qual foi o consumo de combustível: "))

# Aqui Estou dividindo os dois valores (PROCESSO)
KmL = distanciaPercorrida / combustivelConsumido

# E aqui estou mostrando o consumo do veículo para o usuário. E acabei usando .2f, pois essa função mostra a quantidade de casas depois da vírgula vai exibir (SAÍDA)
print(f"O consumo médio de seu veículo é de {KmL:.2f} Km/L")