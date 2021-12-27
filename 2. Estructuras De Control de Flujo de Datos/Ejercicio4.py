# Para un valor entero positivo que representa una cantidad en segundos, indicar
# su equivalente en minutos, horas y días.

segundos = int(input("Ingrese la cantidad de segundos: "))

dias = segundos // (24 * 60 * 60)
segundos = segundos % (24 * 60 * 60)

horas = segundos // (60 * 60)
segundos = segundos % (60 * 60)

minutos = segundos // (60)
segundos = segundos % (60)

print("Tiempo: " + str(dias) + "d - " + str(horas) + "h - " + str(minutos) + "m - " + str(segundos) + "s")
