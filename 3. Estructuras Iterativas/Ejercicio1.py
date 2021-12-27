# #Dado un número entero N, calcular e informar al usuario cuántos dígitos tiene
# dicho número.

numeroEnt = int(input("Ingrese un numero entero: "))
count = 0
while numeroEnt > 0:
    numeroEnt //= 10 
    count += 1
print("El número de dígitos de su número es: {}".format(count))
