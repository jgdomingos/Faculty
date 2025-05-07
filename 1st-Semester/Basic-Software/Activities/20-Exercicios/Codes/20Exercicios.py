# 1) Elaborar um programa que receba dois números inteiros e calcule e mostre a soma desses números.

# As duas linhas a seguir está solicitando os dois números de entrada para o usuário (ENTRADA)
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

# Aqui estou fazendo a soma dos dois números (PROCESSO)
resultado = num1 + num2

# E aqui estou mostrando o resultado para o usuário (SAÍDA)
print(f"O resultado da soma desses dois números é {resultado}")


# 2) Elaborar um programa que receba quatro números inteiros, que calcule e mostre a soma e a média desses números.

# Nas 4 linhas a seguir estou solicitando ao usuário 4 números inteiros (EBTRADA)
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))
num4 = int(input("Insira o quarto número: "))

# Na primeira linha estou fazendo a soma desses 4 números e na segunda linha estou dividindo o resultado da soma por 4 (PROCESSO)
resultadoSoma = num1 + num2 + num3 + num4
resultadoMedia = resultadoSoma / 4

# E aqui estou exibindo uma mensagem com o resultado para o usuário (SAÍDA)
print(f"A soma desses quatros números é {resultadoSoma} \nE a média é {resultadoMedia}")


# 3) Elaborar um programa para calcular o valor de y como função de x, segundo a função y(x)=3x+2, em um domínio real.

# Solicitei o valor de X para o usuário e usei a função Float, pois o usuário pode passar qualquer valor aqui (Real ou Inteiro) (ENTRADA)
numX = float(input("Insira um número: "))

# Aqui está sendo feita a resolução do exercício, fazendo X * 3 primeiro e depois somando com 2 (PROCESSO)
numY = (numX * 3) + 2

# Aqui esta sendo exibido o resultado para o usuário (SAÍDA)
print(f"O resultado da função é {numY}")


# 4) Elaborar um programa que calcule o consumo médio de um automóvel (medido em km/l), dado que são conhecidos a distância total percorrida e o volume de combustível consumido para percorrê-la (medido em litros).

# Nas duas linhas a seguir estou solicitando ao usuário quantos KMs ele rodou e qual foi o consumo de combustível (ENTRADA)
distanciaPercorrida = float(input("Insira quantos Km você rodou: "))
combustivelConsumido = float(input("Insira qual foi o consumo de combustível: "))

# Aqui Estou dividindo os dois valores (PROCESSO)
KmL = distanciaPercorrida / combustivelConsumido

# E aqui estou mostrando o consumo do veículo para o usuário. E acabei usando .2f, pois essa função mostra a quantidade de casas depois da vírgula vai exibir (SAÍDA)
print(f"O consumo médio de seu veículo é de {KmL:.2f} Km/L")


# 5) Elaborar um programa que leia o saldo de uma aplicação e imprimir o novo saldo, considerando um reajuste de 15%.

# Estou solicitando para o usuário o saldo antigo dele (ENTRADA)
saldo = float(input("Insira o seu antigo saldo: "))

# Aqui está sendo feito o calculo, na primeira linha está fazendo o saldo antigo * 0.15 e depois o resultado dessa multiplicação (reajuste) + o saldo antigo (PROCESSO)
reajuste = saldo * 0.15
novoSaldo = reajuste + saldo

# E aqui vai exibir o saldo atual já com o reajuste (SAÍDA)
print(f"O seu reajuste no saldo é de R${novoSaldo}")


# 6) Elaborar um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.

# Estou solicitando o salário atual e o percentual de aumento (ENTRADA)
salario = float(input("Insira seu salário atual: "))
percentual = float(input("Insira qual foi o percentual de aumento: "))

# Aqui está sendo feita a resolução do problema (PROCESSO)
reajuste = salario * (percentual / 100)
novoSalario = salario + reajuste

# Aqui vai exibir o novo salário e o reajuste desse funcionário (SAÍDA)
print(f"Você teve um aumento salarial de R${reajuste} o valor do seu novo salário é de R${novoSalario}")


# 7) Elaborar um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
# - A idade desta pessoa hoje;
# - A idade desta pessoa em 2035

# Estou solicitando o ano de nascimento e o ano atual para o usuário (ENTRADA)
nascimento = int(input("Em qual ano você nasceu? "))
anoAtual = int(input("Insira o ano atual: "))

# Aqui esta acontecendo a resolução, descobrindo a idade da pessoa e quantos anos ela terá em 2035 (PROCESSO)
idadeAtual = anoAtual - nascimento
idadeFutura = 2035 - nascimento

# Aqui estou exibindo a idade dele e a idade que ela terá em 2035 (SAÍDA)
print(f"Você tem {idadeAtual} anos e em 2035 você terá {idadeFutura} anos.")


# 8) Elaborar um programa que dados o tamanho de um arquivo (em bits), bem como a velocidade da conexão (em bits por segundo), informe o tempo necessário para o download do arquivo.

# Aqui estou solicitando pro usuário o tamanho do arquivo e a velocidade de conexão dele, tudo e bits (ENTRADA)
tamanhoDeArquivo = float(input("Qual o tamanho do arquivo? (em bits) "))
velocidadeDeConexao = float(input("Qual a velocidade de conexão? (bits por segundo) "))

# Aqui está divindo o tamanho do arquivo e a velocidade de conexão (PROCESSO)
tempoDeDownload = tamanhoDeArquivo / velocidadeDeConexao

# Aqui esta convertendo o resultado de cima para minutos e segundos (PROCESSO)
minutos = int(tempoDeDownload // 60)
segundos = int(tempoDeDownload % 60)

# Aqui esta mostrando para o usuário o tempo que vai levar para concluir o download (SAÍDA)
print(f"O download do arquivo vai levar {minutos} minutos e {segundos} segundos.")


# ) Elaborar um programa que receba um número positivo e maior que zero, calcule e mostre:
# a) o número digitado ao quadrado;
# b) a raiz quadrada do número digitado;

# Estou importando cálculos matemáticos
import math

# Estou solicitando ao usuário um número positivo e maior que zero (ENTRADA)
numero = int(input("Insira um número positivo e maior que zero: "))

# Nas duas linhas a seguir está calculado o quadrado e a raiz quadrada desse número (PROCESSO)
aoQuadrado = numero * numero
raiz = math.sqrt(numero)

# Aqui estou mostrando o resultado para o usuário (SAÍDA)
print(f"O quadrado desse número é: {aoQuadrado}\nE a raiz quadrada desse número é: {raiz}")


# 10) Elaborar um programa que dados dois lados de um triângulo retângulo calcule e exiba a respectiva hipotenusa

# Estou importando cálculos matemáticos
import math

# Nas duas linhas a seguir estou solicitando ao usuário o tamanho de dois lados desse Triângulo Retângulo. O HYPOT calcula o comprimento da hipotenusa de um triângulo retângulo(ENTRADA)
ladoA = float(input("Digite o tamanho do lado A: "))
ladoB = float(input("Digite o tamanho do lado B: "))

# Aqui está calculando a Hipotenusa (PROCESSO)
hipotenusa = math.hypot(ladoA, ladoB)

# Aqui estou mostrando o resultado para o usuário (SAÍDA)
print(f"A Hipotenusa desse triângulo retângulo é {hipotenusa}")


# 11) Elaborar um programa que calcule a aceleração de um corpo em movimento conhecendo-se as velocidades inicial e final, e o intervalo de tempo medido (a = (v2 –v1)/∆t). Exibir o resultado

# Nas 3 linhas a seguir estou solicitando ao usuário valocidade inicial, final e o intervalo de tempo (ENTRADA)
velocidadeInicial = float(input("Qual é a velocidade inicial? "))
velocidadeFinal = float(input("Qual é a velocidade final? "))
intervaloTempo = float(input("Qual o intervalo de tempo medido? "))

# Aqui está calculando a aceleração do corpo em movimento (PROCESSO)
aceleracao = (velocidadeFinal - velocidadeInicial) / intervaloTempo

# Aqui estou mostrando o resultado para o usuário (SAÍDA)
print(f"A aceleração desse corpo em movimento é de {aceleracao}")


# 12) Elaborar um programa que receba o raio de uma esfera. O algoritmo deve calcular e exibir a área e o volume da esfera

# Estou importando cálculos matemáticos
import math

# Estou solicitando ao usuário o valor do Raio da esfera (ENTRADA)
raio = float(input("Qual é o raio dessa esfera? "))

# Nas duas linhas a seguir está calculando o volume e a área dessa esfera (PROCESSO)
volume = (4 / 3) * math.pi * math.pow(raio, 3)
area = 4 * math.pi * math.pow(raio, 2)

# Aqui estou mostrando o resultado para o usuário (SAÍDA)
print(f"O volume dessa esfera é: {volume}\nA área dessa esfera é {area}")


# 13) Elaborar um programa que receba o raio e a altura de uma lata de óleo para calcular e apresentar o valor do volume desta lata, dado: V = π*r2*h.

# Estou importando cálculos matemáticos
import math

# Nas duas linhas a seguir estou solicitando ao usuário o raio e a altura da lata de óleo (ENTRADA)
raio = float(input("Qual é o raio da lata de óleo? "))
altura = float(input("Qual a altura dessa lata de óleo? "))

# Aqui está calculando o volume da lata de óleo (PROCESSO)
volume = math.pi * math.pow(raio, 2) * altura

# Aqui estou mostrando o resultado para o usuário (SAÍDA)
print(f"O volume dessa lata de óleo é {volume}")


# 14) Elaborar um programa que leia uma temperatura em graus Celsius e deve converter em graus Fahrenheit. A fórmula de conversão é: F = (9*C+160)/5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius. Exibir a temperatura em Fahrenheit.

# Estou solicitando ao usuário a temperatura atual em graus celsius (ENTRADA)
grausCelsius = int(input("Qual a temperatura atual? "))

# Aqui está acontecendo a conversão para Fahrenheit (PROCESSO)
fahrenheit = (9 * grausCelsius + 160) / 5

# Aqui estou mostrando a conversão para o usuário (SAÍDA)
print(f"A tempetatura {grausCelsius}ºC em Fahrenheit é {fahrenheit}ºF")


# 15) Elaborar um programa que leia três números inteiros (A, B, C) e calcule a seguinte expressão: D = R + S / 2 onde R = (A + B)2 e S = (B + C)2. Exibir o valor D.

# Nas 3 linhas a seguir estou solicitando ao usuário 3 números inteiros (ENTRADA)
numero1 = int(input("Qual o valor do número 1? "))
numero2 = int(input("Qual o valor do número 2? "))
numero3 = int(input("Qual o valor do número 3? "))

# Nas 3 linhas a segui esta calculado o valor de R, S e D (PROCESSO)
R = (numero1 + numero2) ** 2
S = (numero2 + numero3) ** 2
D = (R + S) / 2

# Aqui estou mostrando o resultado de D para o usuário (SAÍDA)
print(f"O valor de D é: {D}")


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


# 17) Elaborar um programa que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias.

# Estou solicitando ao usuário quantos anos, meses e dias (ENTRADA)
anos = int(input("Quantos anos você tem? "))
meses = int(input("Quantos meses? "))
dias = int(input("Quantos dias? "))

# Aqui está convertendo esses números para dias totais (PROCESSO)
diasTotais = (anos * 365) + (meses * 30) + dias

# Aqui estou mostrando o resultado em dias totais para o usuário (SAÍDA)
print(f"Você já viveu {diasTotais} dias.")


# 18) Elaborar um programa que leia o tempo de duração de um evento em uma fábrica expressa em segundos e mostre-o expresso em horas, minutos e segundos.

# Aqui estou solicitando o tempo de duração do eventos em segundos (ENTRADA)
duracao = int(input("Qual foi o tempo de duração do evento (Insira em segundos)? "))

# Nas 3 linhas a seguir está fazendo a conversão para Horas, Minutos e Segundos (PROCESSO)
horas = duracao // 3600
minutos = (duracao % 3600) // 60
segundos = duracao % 60

# Aqui estou mostrando o resultado em tempo total para o usuário (SAÍDA)
print(f"O eventos teve uma duração de {horas}:{minutos}:{segundos}")


# 19) Elaborar um programa que calcule o salário líquido de um funcionário, exibindo no final o nome, telefone e o salário líquido, considerando:
# a) os dados do funcionário: nome, RG e telefone.
# b) salário bruto de R$ 2500,00
# c) descontos de R$ 300,00

# Estou solicitando dados pessoais para o usuário (ENTRADA)
nome = input("Qual o seu nome completo? ")
rg = input("Qual o seu RG? ")
telefone = input("Qual o seu número de telefone? ")

# Estou fornecendo ao sistema o salário bruto e o valor do desconto
salarioBruto = 2500.00
desconto = 300.00

# Aqui está calculando o valor so salário líquido do funcionário (PROCESSO)
salarioLiquido = salarioBruto - desconto

# Aqui está mostrando os dados pessoais cadastrados e o salário líquido para o usuário (SAÍDA)
print(f"Nome: {nome}\nRG: {rg}\nTelefone:{telefone}\nSalário Líquido: R${salarioLiquido}")


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