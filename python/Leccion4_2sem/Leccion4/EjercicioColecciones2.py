# Ejercicio 2: Operaciones de conjunto con listas
# Escriba un programa que tenga 2 listas y que a continuación
# cree las siguientes listas (en las que no deben haber repetición)
# 1 Lista de palaras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segundo
# 3 Lista de palabras que aparecen  en la segunda lista, pero no en la primera
# 4 Lista de palabras que aparecen en ambas listas

lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 5]
lista2 = [4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]

# Eliminar los elemetos repetidos de ambas listas con conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2) # Unimos los dos conjuntos
solo1 = list(conjunto1 - conjunto2) # solo muestra el conjunto1
solo2 = list(conjunto2 - conjunto1) # solo muestra el conjunto2
interseccion = list(conjunto1 & conjunto2) # Elementos en ambos conjuntos  que coinsiden

print(f"Lista de palabras que aparecen en las listas: {union}")
print(f"Lista de palabras que aparecen en la primera lista, pero no en la segunda: {solo1}")
print(f"Lista de palabras que aparecen en la segunda lista, pero no en la primera: {solo2}")
print(f"Lista de palabras que aparecen en ambas listas: {interseccion}")