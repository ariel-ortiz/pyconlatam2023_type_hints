from typing import Generic, TypeVar


T = TypeVar('T')


def repite(valor: T, n: int) -> list[T]:
    return [valor] * n


class Stack(Generic[T]):

    datos: list[T]

    def __init__(self) -> None:
        self.datos = []

    def push(self, elemento: T) -> None:
        self.datos.append(elemento)

    def pop(self) -> T:
        return self.datos.pop()

    def is_empty(self) -> bool:
        return len(self.datos) == 0


s = repite('hola', 3)
print(s)


# una_pila: Stack[int] = Stack()
# print(una_pila.is_empty())
# una_pila.push(42)
# una_pila.push('hola')
# print(una_pila.pop().bit_count())
# print(una_pila.is_empty())
