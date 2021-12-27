#Dado un (1) número binario de cuatro (4) dígitos imprimir su bit da paridad. 
# El bit de paridad es 1 si el número de bits 1 es impar y 0 en caso contrario.

numero = int(input("ingrese un numero binario: "))
if numero == 1:
    print("El número es par: {}".format(numero))
else:
    print("El número es impar: {}".format(numero))
