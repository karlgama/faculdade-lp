class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        self.carro = None

    def comprar_carro(self, carro):
        self.carro = carro


class Carro:
    def __init__(self, marca: str, modelo: str, placa: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
