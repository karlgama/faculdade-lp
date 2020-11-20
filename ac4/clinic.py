from datetime import datetime as dt
from abc import ABC


class Pessoa(ABC):
    def __init__(self, nome, rg, cpf, telefone):
        self.nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.telefone = telefone

    def getRg(self):
        return self.__rg

    def getCPF(self):
        return self.__cpf


class Medico(Pessoa):
    def __init__(self, crm, cpf, rg, nome, telefone, salario, especialidade):
        super().__init__(nome, rg, cpf, telefone)
        self.crm = crm
        self.__salario = salario
        self.especialidade = especialidade

    def exibirMedico(self):
        return ("CRM: " + self.crm + " Nome: " + self.nome + " Telefone: "
                + self.telefone +
                " Salário: $" + self.__salario + " Especialide: " +
                self.especialidade)


class Paciente(Pessoa):
    def __init__(self, nome, rg, cpf, endereco, telefone, dataNascimento,
                 medico):
        super().__init__(nome, rg, cpf, telefone)
        self.endereco = endereco
        self.dataNascimento = dataNascimento
        self.medico = medico
        self.estado = {}
        self.quarto = ''

    def atualizarEstado(self, descricao, hora, nomeMedico):
        self.estado[dt.now()] = [hora, descricao, nomeMedico]
        return self.estado

    def exibirPaciente(self):
        return ("Paciente: " + " Endereço: " + self.endereco + " Telefone: " +
                " RG:" + self.getRg() + " CPF:" + self.getCPF() + 
                self.telefone + " Data de nascimento: " + self.dataNascimento +
                " Medico" + " CRM: " + self.medico.crm + " Nome do Médico: " +
                self.medico.nome + " Telefone: " +
                self.medico.telefone + " Especialide: " +
                self.medico.especialidade)

    def getQuarto(self):
        return self.quarto.exibirQuarto()


class Quarto:
    def __init__(self, numero, andar):
        self.numero = numero
        self.andar = andar
        self.paciente = ' '

    def internar(self, paciente):
        self.paciente = paciente
        self.paciente.quarto = self
        return("Paciente internado no quarto número: " + self.numero +
               " No andar: " + self.andar)

    def exibirQuarto(self):
        return ("Quarto: " + self.numero + " Andar: " + self.andar)