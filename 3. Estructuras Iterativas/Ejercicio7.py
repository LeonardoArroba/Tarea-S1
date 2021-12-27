# Se tiene una secuencia de enteros terminada en cero, que corresponde a la edad,
# peso y estatura de una muestra de hombres y mujeres mayores de 18 años. Con
# base en dicha secuencia se desea realizar un estudio a fin de conocer:
# Edad promedio de todas las personas en la muestra.
# Peso promedio de todas las personas en la muestra.
# Estatura promedio de todas las personas en la muestra.
# Cuántas personas hay con edad entre los 18 y 25 años.
# Cuántas personas son mayores a 36 años.
# Cuál es el promedio de peso de las personas con edades entre 18 y 35
# años.

suma, suma1, suma2, suma3, suma4, suma5 = 0, 0, 0, 0, 0, 0
contador, cont1, cont2 , cont3, cont4, cont5 = 0, 0, 0, 0, 0, 0
edad = 1 
peso = 1
estatura = 1

while edad != 0 and peso != 0 and estatura !=0:
    edad = int(input("Ingrese la edad de una persona: "))
    peso = int(input("Ingrese el peso de una persona: "))
    estatura = float(input("Ingrese la estatura de una persona: "))
    if edad != 0:
        suma += edad
        contador += 1
    if peso != 0:
        suma1 += peso
        cont1 += 1
    if estatura != 0:
        suma2 += estatura
        cont2 += 1
    if edad != 0:
        if 18 <= edad <= 25:
            suma3 += edad
            cont3 += 1
    if edad != 0:
        if edad >= 36:
            suma4 += edad
            cont4 += 1
    if peso != 0:
        if 18 <= edad <= 35:
            suma5 += peso
            cont5 += 1
if contador == 0 and cont1 == 0 and cont2 == 0 and cont3 == 0:
    print("No digito ningun numero.")
else:
    promedio = suma / contador
    print("El promedio de las edades de todas las personas es: {}".format(promedio))
    prome1 = suma1 / cont1
    print("El promedio del peso de todas las personas es: {}".format(prome1))
    prome2 = suma2 / cont2
    print("El promedio de la estatura de todas las personas es: {}".format(prome2))
    prome3 = suma3 / cont3
    print("El promedio de la edad entre los 18 y 25 años es: {}".format(prome3))
    prome4 = suma4 / cont4
    print("El promedio de las personas mayores a 36 años: {}".format(prome4))
    prome5 = suma5 / cont5
    print("El promedio del peso de las personas con edades entre 18 y 35 años: {}".format(prome5))