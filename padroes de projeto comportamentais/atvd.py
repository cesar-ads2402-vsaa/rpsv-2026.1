from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def calcular(self, a, b):
        pass


class Soma(Strategy):
    def calcular(self, a, b):
        return a + b


class Multiplicacao(Strategy):
    def calcular(self, a, b):
        return a * b


class Calculadora:
    def __init__(self, estrategia: Strategy):
        self.estrategia = estrategia

    def calcular(self, a, b):
        return self.estrategia.calcular(a, b)


if __name__ == "__main__":
    calc = Calculadora(Soma())
    print(calc.calcular(5, 3))

    calc = Calculadora(Multiplicacao())
    print(calc.calcular(5, 3))