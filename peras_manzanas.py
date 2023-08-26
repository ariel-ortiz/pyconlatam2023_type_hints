from __future__ import annotations


class Frutas:

    cantidad: int

    def __init__(self, cantidad: int = 1) -> None:
        self.cantidad = cantidad

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.cantidad})'


class Manzanas(Frutas):
    pass


class Peras(Frutas):

    def __add__(self, otras: Peras) -> Peras:
        return Peras(self.cantidad + otras.cantidad)


# una_pera = Peras()
# otra_pera = Peras()
# dos_peras = una_pera + otra_pera
# print(f'{dos_peras = }')

# una_manzana = Manzanas()
# mezcolanza = una_pera + una_manzana
# print(f'{mezcolanza = }')
