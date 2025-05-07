# 6) Elaborar um algoritmo que o usuário tenha que digitar 10 números inteiros. No final, o programa deve exibir quantos números são múltiplos de 3, quantos números são menores que 45 e maiores que 55, e qual é o menor número entre eles
 
valores = []
 
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    valores.append(num)

multiplos3 = sum(1 for n in valores if n % 3 == 0)
entre45e55 = sum(1 for n in valores if n < 45 or n > 55)
menorNumero = min(valores)

print(f"Quantidade de múltiplos de 3: {multiplos3}")
print(f"Quantidade de números menores que 45 e maiores que 55: {entre45e55}")
print(f"Menor número digitado: {menorNumero}")