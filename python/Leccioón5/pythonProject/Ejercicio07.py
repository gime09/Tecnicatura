# Ejercicio 7: Juego adivina el número
# Realizar un juego para adivinar un número. Para ello se debe
# Generar un número aleatorio entre 1-100, y luego ir pidiendo
# números indicando "es mayo" o "es menor" según sea mayor o menor
# Con respecto a N . El proceso termina cuando el usuario acierta
# y allí se debe mostrar el número de intentos.

import random

print("\t.: Juego Adivina el número:.")
aleatorio = random.randint(0,100) # Toma de 0 a 100 literal, generamos un número aleatorio
contador = 0
while True:
    numero = int(input("Digite uhn n número: "))
    contador += 1
    if numero > aleatorio:
        print("\tNo es el número, digite un  número menor")
    elif numero < aleatorio:
        print("\tNo es el número digite un numero mayor ")
    else:
        print(f"FELICIDADES, acabas de adivinar el número {aleatorio}")
        break # Rompe el ciclo y el bucle

print(f"\nNúmero de intentos: {contador}")

