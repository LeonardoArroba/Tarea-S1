# Dado un número, determine si es capicúa.
# Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás.

numero = int(input("ingrese un numero positivo: "))

if numero >= 0:
    if str(numero) == str(numero)[::-1]:
        print("{} es capicúa".format(numero))
    else:
        print("{} no es capicúa".format(numero))
else:
    print("El numero debe ser positivo")
