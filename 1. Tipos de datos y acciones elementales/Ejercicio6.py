#Dado un (1) número, imprimir 0 si es par y 1 si es impar. 
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")