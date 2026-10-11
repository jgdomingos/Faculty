class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    # Método
    def andar(self):
        print("Estou andando e meu nome é:", self._nome)

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def estudar(self):
        print("Oi eu sou", self._nome, "Estou estudando")

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

aluno1 = Aluno("Universidade", 81, 123456)
Professor1 = Professor("Ana", 50, "Engenharia de Software")

Professor1.andar()
aluno1.estudar()