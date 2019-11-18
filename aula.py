from abc import ABCMeta, abstractmethod


class Programas(metaclass=ABCMeta):
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @abstractmethod
    def __str__(self):
        return f"{self._nome}, {self.ano} ({self.likes} likes)"

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1


class Filme(Programas):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duração = duracao

    def __str__(self):
        return super().__str__() + f" | {self.duração} min"


class Serie(Programas):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return super().__str__() + f"| {self.temporadas} temporadas"


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()


atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()


demolidor = Serie("demolidor", 2016, 2)
demolidor.dar_like()
demolidor.dar_like()

tmep = Filme("todo mundo em panico", 1999, 100)
tmep.dar_like()

playlist = [vingadores, atlanta, demolidor]
playlist = Playlist("fds", playlist)
for programa in playlist:
    print(programa)

print(f"tamanho da playlist: {len(playlist)}")
