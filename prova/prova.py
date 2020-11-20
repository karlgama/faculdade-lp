class Copo:
    def __init__(self, capacidade: int, quantidade: int):
        self.__quantidade = quantidade
        self.__capacidade = capacidade

    def get_quantidade(self):
        return self.__quantidade

    def get_capacidade(self):
        return self.__capacidade

    def encher(self):
        if(self.__quantidade >= self.__capacidade):
            print("Copo já está cheio!")
        else:
            self.__quantidade += 100
        return self.__quantidade

    def esvaziar(self):
        if(self.__quantidade <= 0):
            print("Copo já está vazio")
        else:
            self.__quantidade -= 100
        return self.__quantidade


copo = Copo(400, 200)

copo.encher()
print("Quantidade:", copo.get_quantidade())    # Quantidade: 300
copo.encher()
print("Quantidade:", copo.get_quantidade())    # Quantidade: 400
copo.encher()
print("Quantidade:", copo.get_quantidade())    # Quantidade: 400

copo.esvaziar()
print("Quantidade:", copo.get_quantidade())    # Quantidade: 300
copo.esvaziar()
print("Quantidade:", copo.get_quantidade())    # Quantidade: 200
copo.esvaziar()
print("Quantidade:", copo.get_quantidade())    # Quantidade: 100
copo.esvaziar()
print("Quantidade:", copo.get_quantidade())    # Quantidade: 0
copo.esvaziar()
print("Quantidade:", copo.get_quantidade())    # Quantidade: 0
copo.esvaziar()
