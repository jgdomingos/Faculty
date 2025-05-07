# 7) Faça um algoritmo que leia os dois valores inteiros A e B se os valores forem iguais deverá se somar os dois, caso contrário multiplique A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.

# Aqui estou solicitando ao usuário o valor de A e B (ENTRADA)
A = int(input("Digite um valor: "))
B = int(input("Digite um valor: "))

# Aqui está verificando se os valores são iguais, se forem iguais vai somar, senão vai multiplicar (CONDIÇÃO)
if ( A == B ):
    C = A + B
    print(F"{C}") # (SAÍDA)
else:
    C = A * B
    print(f"{C}") # (SAÍDA)