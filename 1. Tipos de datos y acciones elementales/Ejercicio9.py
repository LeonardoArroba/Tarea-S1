# Dado un (1) número de cuatro (4) dígitos imprimirlo por separado en unidades,
# decenas, centenas y unidades de mil.
# Entrada:
# 1234
# Salida:
# Unidades: 4
# Decenas: 3
# Centenas: 2
# Unidades de mil: 1

numero = int(input("Ingresar un numero: "))
Umil = numero / 1000
tmp = numero % 1000

centenas = tmp / 100
tmp = tmp % 100

decenas = tmp / 10

unidades = tmp % 10

print("Unidades: {}".format(int(unidades)))
print("Decenas: {}".format(int(decenas)))
print("Centenas: {}".format(int(centenas)))
print("Unidades de mil: {}".format(int(Umil)))



