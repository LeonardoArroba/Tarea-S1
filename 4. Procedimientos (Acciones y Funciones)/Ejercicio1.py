# Construya una función que solicite edades al usuario y determine el promedio de
# las edades mayores a 18 años. El usuario indicará cuando desea dejar de
# suministrar datos de entrada. En la Acción Principal se informará el promedio
# calculado.

def edades():
    suma = 0
    contador = 0
    edad = 1
    while edad != 0:
        edad = int(input("Digite un numero entero (0 para terminar): "))
        if edad != 0:
            if edad > 18:
                suma += edad
                contador += 1
    if contador == 0:
        print("No digito ningun numero.")
    else:
        promedio = suma / contador
        print("El promedio de edades mayores a 18 años es: {}".format(promedio))
edades()