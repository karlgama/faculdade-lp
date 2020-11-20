class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_salario(self):
        return self.__salario


func1 = Funcionario("Pedro", "111222333-22", 1500.0)
func1.salario = 2000.0              # Altera o salário
print("Nome:", func1.get_nome())
print("CPF:", func1.get__cpf())
print("Salário:", func1.get__salario())
