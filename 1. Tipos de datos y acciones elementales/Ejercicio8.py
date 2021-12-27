# Dado un (1) número binario de cuatro (4) dígitos imprimir su valor
numeroBi = input("Ingrese el numero binario: ")
cad = numeroBi[::-1]
sald = 0 ; expon = 0

while expon < len(cad):
    if int(cad[expon]) == 1:
        sald += int(cad[expon]) * 2 ** expon
    expon += 1
print("El resultado es: {}".format(sald))