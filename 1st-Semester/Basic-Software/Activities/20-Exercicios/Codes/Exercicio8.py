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