class Orden:
    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        self.computadoras = computadoras

    def agregar_computadora(self, computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ""
        for computadora in self.computadoras:
            computadoras_str += computadora.__str__()
        return f"Orden: {self.id_orden}\n" \
               f"Computadoras:\n" + computadoras_str