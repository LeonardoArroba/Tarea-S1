# Dado un número N determinar si es un número primo.
# Nota: Un número primo es aquel que solo es divisible por 1(uno) y por el mismo.

numero = int(input("Ingrese un numero: "))
esPrimo = True
for i in range(2, numero):
    if numero % i == 0:
        esPrimo = False
        break
if esPrimo:
    print("El numero {} es primo".format(numero))
else:
    print("El numero {} no es primo".format(numero))
    