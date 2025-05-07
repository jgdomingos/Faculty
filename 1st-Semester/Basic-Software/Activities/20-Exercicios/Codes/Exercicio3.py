# 3) Elaborar um programa para calcular o valor de y como função de x, segundo a função y(x)=3x+2, em um domínio real.

# Solicitei o valor de X para o usuário e usei a função Float, pois o usuário pode passar qualquer valor aqui (Real ou Inteiro) (ENTRADA)
numX = float(input("Insira um número: "))

# Aqui está sendo feita a resolução do exercício, fazendo X * 3 primeiro e depois somando com 2 (PROCESSO)
numY = (numX * 3) + 2

# Aqui esta sendo exibido o resultado para o usuário (SAÍDA)
print(f"O resultado da função é {numY}")