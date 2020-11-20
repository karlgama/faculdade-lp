# ALUNO 1: Kaique Silva Grangeiro RA:1903564
# ALUNO 2: Ricardo Antônio Gonçalves da Silva RA: 1903013
# ALUNO 3: Felipe Freire Lopes RA: 1903226

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.casas = []

    def get_nome(self):
        return self.nome

    def get_casa(self):
        return self.casa

    def set_nome(self, nome):
        self.nome = nome

    def set_casa(self, casas):
        self.casas = casas

    def incluir_casa(self, casa):
        self.casas.append(casa)


class Casa:
    def __init__(self, nome):
        self.nome = nome
        self.__diretor = None
        self.__monitor = None

    def set_diretor(self, diretor):
        self.__diretor = diretor

    def set_monitor(self, monitor):
        self.__monitor = monitor

    def get_diretor(self):
        return self.__diretor

    def get_monitor(self):
        return self.__monitor


class Professor:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
        self.disciplinas = []

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)


class Aluno:
    def __init__(self, nome, nascimento, tipo):
        self.nome = nome
        self.nascimento = nascimento
        self.tipo = tipo
        self.__casa = None
        self.__triunfos = 0
        self.__mau_feitos = 0 

    def set_casa(self, casa):
        self.casa = casa

    def get_casa(self):
        return self.casa 

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome 

    def incluir_triunfo(self, quantidade):
        self.__triunfos = int(self.__triunfos + quantidade)

    def incluir_mau_feito(self, quantidade):
        self.__mau_feitos = int(self.__mau_feitos + quantidade)

    def get_triunfo(self):
        return self.__triunfos

    def get_mau_feito(self):
        return self.__mau_feitos


class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def get_nome(self):
        return self.nome

    def get_alunos(self):
        return self.alunos

    def set_alunos(self, alunos):
        self.alunos = alunos

    def set_nome(self, nome):
        self.nome = nome

    def incluir_aluno(self, aluno):
        self.alunos.append(aluno)
