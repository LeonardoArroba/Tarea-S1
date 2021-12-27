# Todos los años que se dividen exactamente entre 400, o que son divisibles
# exactamente entre 4 y no son divisibles exactamente entre 100 son años bisiestos.
# Usando estas premisas crea un algoritmo que lea una fecha como un número
# entero con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si
# el mismo es un año bisiesto o no.
dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))
print(str(dia) + "/" + str(mes) + "/" + str(año))
if año % 4 == 0 and año % 100 != 0:
    print("El año " + str(año) + " si es bisiesto")
elif año % 100 == 0 and año % 400 == 0:
    print("El año " + str(año) + " si es bisiesto")
else:
    print("El año " + str(año) + " no es bisiesto")

