# Lista = Ariel, Liliana, Natalia, Osvaldo (Se puede tener cualquier tipo de datos)
# El índice comienza desde cero

nombres = ["Naty", "Osvaldo", "Lily", "Ariel"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])
print(nombres[0:2]) # Sólo muestra el indice 0, 1 pero no el indice 2
# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3]) # Indice a mostrar 0, 1, 2
# Desde el indice indicado hasta el final
print(nombres[1:])
# Modificamos un valor
nombres[2]="Liliana"
nombres[0]="Natalia"
print(nombres)
#Iterara una lista
for nombre in nombres: #nombre en singular, la lista es plural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")
 # Preguntamos cuántos elementos tiene
print(len(nombres)) #len funcion que regresa la cantidad de elementos de una lista, pasamos por parametros nuestra lista

#Agregamos un elemento
nombres.append("Marcelo") # cola, ingresa al final
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)


# Insertar un elemento en un indice especifico
nombres.insert(1,"Alberto")
print(nombres)
nombres.insert(3,"Debora")
print(nombres)

#Eliminamos un elemento
nombres.remove("Alberto")
print(nombres)
#Eliminamos el último elemento
nombres.pop()
print(nombres)
#Eliminar un índice especifiico
del nombres[2] # del , delete (eliminar)
print(nombres)
#Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)
#Eliminar la lista
del nombres
# print(nombres) #Aquí nos mostrará este error

#Definimos una tupla (NO puede haber modificaciones)
cocina=("cuchara", "cuchillo", "tenedor")
print(cocina)
print(len(cocina))
# Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])
# mostrar de manera inversa
print(cocina[-1])
# Acceder a un rango
print(cocina[0:1])
print(cocina[0:2])
#Ejemplo
verduras = ("papa",) # no es tupla es de tipo string  si no tiene la coma ,
# Recorremos los elementos de la tupla
for cocinar in cocina: # Print esta usando \n para saltos de líneas
    print(cocinar, end=" ") # Usamos end= para eliminar saltos de líneas

cocinaLista = list(cocina)
cocinaLista[0] = "Plato"
cocina = tuple(cocinaLista)
print("\n", cocina)
# del cocina es para eliminar la tupla

# Tipo set (orden aleatorio porque no hay indice)
planetas = {"Marte", "Júpiter", "Venús"}
print(planetas)
print(len(planetas)) # len = siginifica largo

# Revisar si un elemento existe dentro de set
print("Marte" in planetas)
print("Júpiter" not in planetas)

# Agregar un elemento (No se puede agregar un elemento duplicado o repetido)
planetas.add("Tierra") # add es una función
print(planetas)

# Eliminar elementos, puede arrojar un erro si el elemento no existe
planetas.remove("Júpiter") # Esta función ante un mal ingreso u inexistencia del elemento da error
print(planetas)
planetas.discard("tierra") # Esta función no nos presenta ningun error ante un mal ingreso, pero no  borra el elemento
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

# Eliminar set o conjunto
# del planetas
# print(planetas) # Al eliminar nos muestra un error

# "Maradona" :10 Un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(Key,value)
diccionario = {
    "IDE": "Integrated Development Environment",
    "POO": "Programación Orientada a Objetos",
    "SABD": "Sistema de Administración de Base de Datos"

}
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con la llave(Key)
print(diccionario["IDE"])

#Otra forma de recuperar un elemento
print(diccionario.get("POO"))
print(diccionario.get("SABD"))

# Modificamos elementos
diccionario["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: # Recorremos mostrando solo las llaves
    print(termino)


# Necesitamos una función para recorrer un diccionario
for termino, valor  in diccionario.items():
    print(termino, valor)

# Otra manera de acceder a un diccionario
for termino in diccionario.keys(): # Estamos usando una función
    print(termino) # Muestra solo las llaves

for valor in diccionario.values(): # Usamos una función para acceder al valor
    print(valor)

#Comprobar la exixtencia de algún elemento
print("IDE" in diccionario) # devuelve un booleano

# Agregar un elemento
diccionario["PK"] = "Primary Key"
print(diccionario)

# Eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario # El diccionario se borro

# Concatenar Listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2 # Concatenación
print(lista3)

lista3.extend([7, 8, 9, 1]) # Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # Función para ubicar en que indice esta el valor imgresado
# print(lista3.index(0)) # Esto daría un error por no ser el elemento parte de la lista

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay dentro de la lista

# Para poner al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Métodos de ordenamiento (Es una función)
lista3.sort() # Oedena los elemento ascendentemente
print(lista3)
lista3.sort(reverse=True) # Ordena descendentemente
print(lista3)

# Repaso de Tuplas
tupla = (4, "Hola", 6.78, [1, 2, 78], 4, "Hola") # Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) # Acción booleana,su respuesta es de tipo booleana
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

# Repso de set o conjunto
# para definir un conjunto
conjunto2 = set()
conjunto1 = {"bye", }
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add("hola")
print(conjunto1)
print(3 not in conjunto1) #Preguntamos si el número 3 NO esta en el conjunto1

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2)

#Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # La línea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta en el conjunto1 y no  en el conjunto2
print(conjunto3)

conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # Elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Aquí preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) # Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) # No hay cosas en comun

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto

# Repaso de Diccionarios
diccionarioNuevo = {"Azul": "Blue", "Rojo": "Red", "Verde": "Green", "Amarrillo": "Yellow"}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo["Azul"])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {"Ariel": {"Edad": 40, "Altura": 1.83}, "Osvaldo": [45, 1.85], "Natalia": [35, 1.67]}
print(diccionario2)

# Tarea
seleccionArgentina = {
    10: {"Nombre": "Lionel Messi", "Edad": 35, "Altura": 1.70, "Precio": "50 Millones", "Posición": "Extremo Derecho"},
    11: {"Nombre": "Ángel Di María", "Edad": 34, "Altura": 1.80, "Precio": "12 Millones", "Posición": "Extremo Derecho"},
    21: {"Nombre": "Paulo Dybala", "Edad": 28, "Altura": 1.77, "Precio": "35 Millones", "Posición": "Media Punta"},
    19: {"Nombre": "Nicolás Otamendi", "Edad": 34, "Altura": 1.83, "Precio": "3.5 Millones", "Posición": "Defensa Central"},
    1:  {"Nombre": "Franco Armani", "Edad": 35, "Altura": 1.89, "Precio": "3.5 Millones", "Posición": "Portero"},
    7:  {"Nombre": "Rodrigo De Paul", "Edad": 29, "Altura": 1.80, "Precio": 40000000, "Posición": "Centrocampista"},
    9:  {"Nombre": "Julián Álvarez", "Edad": 24, "Altura": 1.70, "Precio": 70000000, "Posición": "Delantero"},
    22: {"Nombre": "Lautaro Martínez", "Edad": 24, "Altura": 1.74, "Precio": 85000000, "Posición": "Delantero"},
    23: {"Nombre": "Emiliano Buendía", "Edad": 26, "Altura": 1.72, "Precio": 35000000, "Posición": "Centrocampista"}
}
print(seleccionArgentina)
print(seleccionArgentina[10])
print(seleccionArgentina.values())

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

for llave in seleccionArgentina:
        print(llave)

for valor in seleccionArgentina.values():
        print(valor)

for llave, valor in seleccionArgentina.items():
        print(llave, valor)

print("Tenemos cargados en el diccionario la cantidad de jugadores: ", end=" ")

print(len(seleccionArgentina))

# Pilas usando lista
pila = [1, 2, 3]

# Agregamos elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
pila.pop()
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop() # Quita el último elemento y lo guarda en la variable
print(f"Sacamos el elemento {elementoBorrado}")
print(f"La pila ahora queda así: {pila}")

# Colas con listas
# Estructura de datos de tipo fifo(first input / first output)
cola = ["Ariel", "Osvaldo", "Liliana", "Pilar"]

#Agregamos elementos al final de la cola
cola.append("Natalia")
cola.append("José")
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

# Seguimos mostrando como recorrer un diccionario con el ciclo for
for i in seleccionArgentina:
    print(f"{i} -> {seleccionArgentina}")




































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































