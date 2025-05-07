# 3) Elaborar um algoritmo que recebe 3 valores (A, B e C) e exibe qual é o maior entre eles. Esse programa deve-se repetir 20 vezes
 
for rep3 in range(1,21):
    A = float(input("Qual o valor de A? "))
    B = float(input("Qual o valor de B? "))
    C = float(input("Qual o valor de C? "))
    if (A > B and A > C):
        print(f"A é o maior valor {A}")
    elif(B > A and B > C):
        print(f"B é o maior valor {B}")
    elif (C > A and C > B):
        print(f"C é o maior valor {C}")
    else:
        print("Os valores são iguais")