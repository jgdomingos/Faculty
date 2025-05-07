# 6) Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja "F" e estado civil seja "CASADA", solicitar o tempo de casada (anos)

# Aqui estou solicitando os dados ao usuário (ENTRADA)
nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo: (F = Feminino | M = Masculino) ")
estadoCivil = input("Digite seu estado civil: ")

# Aqui está verificando o sexo e estado civil da pessoa, caso seja F e CASADA, o programa pergunta quantos anos de casado (CONDIÇÃO)
if (sexo == "F" and estadoCivil == "casada"):
    input("quantos anos de casado? ")