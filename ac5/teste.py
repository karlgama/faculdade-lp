class Episodio:
    def init(self, numero, temporada, nome, duracao):
        self.numero = numero
        self.temporada = temporada
        self.nome = nome
        self.duracao = duracao

class Serie:
    def init(self, nome):
        self.nome = nome

    def incluir_episodio(self, episodio):
        self.episodio = episodio.append[episodio]

    def buscar_episodios(self, temporada):
        capitulos = []
        for ep in self.episodio:
            if ep.temporada == temporada:
                capitulos.append(ep)
        return(capitulos)