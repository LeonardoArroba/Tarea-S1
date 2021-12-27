# Dada una secuencia de números terminada en cero (0), elaborar un algoritmo que
# informe al usuario qué valor tiene el número mayor y qué valor tiene el número
# menor, sin contar el cero (0).

lista = [1,2,5,9,98,25,0]
menor = None
mayor = None
for numero in lista:
    if menor == None and mayor == None:
        menor = numero
        mayor = numero
    else: 
        if numero < menor and numero > 0:
            menor = numero
        if numero > mayor and numero > 0:
            mayor = numero
print("El numero menor es: {}".format(menor))
print("El numero mayor es: {}".format(mayor))
