class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    # Getter para ancho
    @property
    def ancho(self):
        return self._ancho

    # Setter para ancho
    @ancho.setter
    def ancho(self, ancho):
        if ancho > 0:  # Ejemplo de validación
            self._ancho = ancho
        else:
            raise ValueError("El ancho debe ser mayor que 0")

    # Getter para alto
    @property
    def alto(self):
        return self._alto

    # Setter para alto
    @alto.setter
    def alto(self, alto):
        if alto > 0:  # Ejemplo de validación
            self._alto = alto
        else:
            raise ValueError("El alto debe ser mayor que 0")

    def __str__(self):
        return f"FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]"

