
def calcular_estacion(mes):
    if mes in [1, 2, 3]:
        return "Verano"
    elif mes in [4, 5, 6]:
        return "Otoño"
    elif mes in [7, 8, 9]:
        return "Invierno"
    elif mes in [10, 11, 12]:
        return "Primavera"
    else:
        return None

# Pedir al usuario que ingrese un mes del año
mes = int(input("Ingrese un mes del año (1-12): "))

# Calcular y mostrar la estación del año
estacion = calcular_estacion(mes)
if estacion:
    print(f"El mes {mes} corresponde a la estación: {estacion}")
else:
    print("Mes inválido. Por favor, ingrese un valor entre 1 y 12.")

# Ejercicio 4: Etapas de Vida
def etapa_de_vida(edad):
    if 0 <= edad <= 10:
        return "La infancia es increíble y bella"
    elif 10 < edad <= 19:
        return "Tienes muchos cambios, mucho que estudiar"
    elif 20 <= edad <= 29:
        return "Amor y comienza el trabajo"
    else:
        return " Estas en el mejor momento de tu vida ."

# Solicitar la edad al usuario
edad = int(input("Ingresa tu edad: "))
print(etapa_de_vida(edad))

#Ejercicio 5: Sistema de Calificaciones

def calcular_estacion(mes):
    if mes in [1, 2, 3]:
        return "Verano"
    elif mes in [4, 5, 6]:
        return "Otoño"
    elif mes in [7, 8, 9]:
        return "Invierno"
    elif mes in [10, 11, 12]:
        return "Primavera"
    else:
        return None

# Pedir al usuario que ingrese un mes del año
mes = int(input("Ingrese un mes del año (1-12): "))

# Calcular y mostrar la estación del año
estacion = calcular_estacion(mes)
if estacion:
    print(f"El mes {mes} corresponde a la estación: {estacion}")
else:
    print("Mes inválido. Por favor, ingrese un valor entre 1 y 12.")
