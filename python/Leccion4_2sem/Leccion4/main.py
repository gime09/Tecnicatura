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
print(nombres) #Aquí nos mostrará este error