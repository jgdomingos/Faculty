#classe
#objeto
#atributo
#método
#encapsulamento
#herança


# Classe
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    # Método
    def apresentar(self):
        print("Oi eu sou", self._nome)

# Classe
class Aluno(Pessoa): # A classe Aluno esta herdando os atributos da classe Pessoa
    def estudar(self):
        print("Estou estudando há", self._idade, "horas")

aluno1 = Aluno("UMC", 80)

aluno1.apresentar()
aluno1.estudar()