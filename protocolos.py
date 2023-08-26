from typing import Protocol


class Patocolo(Protocol):

    def camina(self) -> str: pass

    def grazna(self) -> str: pass

    def nada(self) -> str: pass


class PatoSalvaje:

    def camina(self) -> str:
        return 'Soy un pato salvaje caminando'

    def grazna(self) -> str:
        return 'Cua, cua, cua...'

    def nada(self) -> str:
        return 'Soy un pato salvaje nadando'


class PatitoDeHule:

    def nada(self) -> str:
        return 'Soy un patito de hule nadando'


def ejecuta_patocolo(p: Patocolo) -> None:
    print(p.camina())
    print(p.grazna())
    print(p.nada())


# un_pato = PatoSalvaje()
# ejecuta_patocolo(un_pato)

# un_patito_de_hule = PatitoDeHule()
# ejecuta_patocolo(un_patito_de_hule)
