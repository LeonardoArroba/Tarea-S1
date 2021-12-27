#Dado un número entero cuya cantidad de dígitos es igual a 5, determine si es capicúa.
numero = int(input("Ingrese un número entero: "))
if numero >= 0:
    if str(numero) == str(numero)[::-1]:
        print(str(numero) + " es capicúa")
    else:
        print(str(numero) + " no es capicúa")
else:
    print("El numero debe ser positivo")
    