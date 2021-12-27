# Cree un algoritmo que tome por entrada las horas y minutos de un día y dé como
# resultado su equivalente en segundos.
horas = int(input("Ingrese la cantidad de horas: "))
minutos = int(input("Ingrese la cantidad de minutos: "))
segundos = int(input("Ingrese la cantidad de segundos: "))

segundos += horas * 60 * 60
segundos += minutos * 60

print("La cantidad de segundos es igual:" + str(segundos))
