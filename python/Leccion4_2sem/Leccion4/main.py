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
