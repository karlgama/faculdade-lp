class Episodio:
    def __init__(self, numero_episodio, numero_temporada, nome_episodio, duracao_min):
        self.numero_episodio = numero_episodio
        self.numero_temporada = numero_temporada
        self.nome_episodio = nome_episodio
        self.duracao_min = duracao_min


class Serie: 
    def __init__(self, nome_serie):
        self.nome_serie = nome_serie
        self.episodios = []

    def incluir_episodio(self, episodio):
        self.episodios.append(episodio)

    def buscar_episodios(self, numero_temporada):
        cap = []
        for ep in self.episodios:
            if ep.numero_temporada == temporada:
                cap.append[ep]
        return(cap)

# ----------------------- PROGRAMA PRINCIPAL ----------------------- #

serie1 = Serie("Game of Thrones")

ep1 = Episodio(1, 1, "Winter Is Coming", 63)
ep2 = Episodio(2, 1, "The Kingsroad", 56)
ep3 = Episodio(3, 1, "Lord Snow", 103)
ep4 = Episodio(1, 8, "Winterfell", 54)
ep5 = Episodio(2, 8, "A Knight of the Seven Kingdoms", 58)
ep6 = Episodio(3, 8, "The Long Night", 82)

serie1.incluir_episodio(ep1)
serie1.incluir_episodio(ep2)
serie1.incluir_episodio(ep3)
serie1.incluir_episodio(ep4)
serie1.incluir_episodio(ep5)
serie1.incluir_episodio(ep6)

serie2 = Serie("Stranger Things")

ep1 = Episodio(1, 1, "Chapter One: The Vanishing of Will Byers", 47)
ep2 = Episodio(2, 1, "Chapter Two: The Weirdo on Maple Street", 55)
ep3 = Episodio(3, 1, "Chapter Three: Holly, Jolly", 51)
ep4 = Episodio(1, 2, "Chapter One: MADMAX", 48)
ep5 = Episodio(2, 2, "Chapter Two: Trick or Treat, Freak", 56)
ep6 = Episodio(3, 2, "Chapter Three: The Pollywog", 51)

serie2.incluir_episodio(ep1)
serie2.incluir_episodio(ep2)
serie2.incluir_episodio(ep3)
serie2.incluir_episodio(ep4)
serie2.incluir_episodio(ep5)
serie2.incluir_episodio(ep6)

# Exibe o nome de todos os episódios da 8ª temporada de Game of Thrones
lista = serie1.buscar_episodios(8)
for ep in lista:
    print(ep.nome)

# Exibe o nome de todos os episódios da 1ª temporada de Stranger Things
lista = serie2.buscar_episodios(1)
for ep in lista:
    print(ep.nome)