from abc import ABC, abstractmethod
# ABC significa: Abstract Base Class, convierte una clase en abstracta


class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            self.ancho = 0
            print(f"Valor erroneo para el ancho: {ancho}")
        if self._validar_valores(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f"Valor erroneo para el alto: {alto}")

    # Getter para ancho
    @property
    def ancho(self):
        return self._ancho

    # Setter para ancho
    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            print(f"valor erroneo ancho: {ancho}")

    # Getter para alto
    @property
    def alto(self):
        return self._alto

    # Setter para alto
    @alto.setter
    def alto(self, alto):
       if self._validar_valores(alto):
           self._alto = alto
       else:
           print(f"valor erroneo alto: {alto}")

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f"FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]"

    def _validar_valores(self, valor): # Método encapsulado
        return True if 0 < valor < 10 else False