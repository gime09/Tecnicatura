class Persona:  # Creamos una clase
    def __init__(self, nombre, apellido, edad):  # Constructor de la clase
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrar_detalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")



# Creamos una instancia de Persona con valores predeterminados
persona1 = Persona("Juan", "Zalazar", 22) # Argumentos
# Imprimimos los atributos de la instancia
print(persona1.nombre)  # Imprime "Juan"
print(persona1.apellido)  # Imprime "Zalazar"
print(persona1.edad)  # Imprime 22

# Creamos otra instancia de Persona con valores diferentes
persona2 = Persona("Ana", "Gómez", 30)
# Imprimimos los atributos de la segunda instancia
print(persona2.nombre)  # Imprime "Ana"
print(persona2.apellido)  # Imprime "Gómez"
print(persona2.edad)  # Imprime 30

persona3 = Persona("Osvaldo", "Giordanini", 45)
print(f"El objeto3 de la clase persona:{persona3.nombre} {persona3.apellido} Su edad es: {persona3.edad}")

# TAREA
persona1 = Persona("Juan", "Zalazar", 22)
print(f"El objeto1 de la clase persona:{persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")

persona1.nombre = "Liliana"
persona1.apellido = "Buccella"
persona1.edad = 40
print(f"El objeto1 modificado de la clase persona:{persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")

# Los atributos son : caracteristicas
# Los métodos (= que una función, pero al metodo se lo asocia con una clase y la función no es propia de si misma) son: el comportamiento que van a tener los objetos (acciones)

persona1.mostrar_detalle()
persona2.mostrar_detalle()