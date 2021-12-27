import datetime
# Escriba un algoritmo que reciba una fecha (día y mes) correspondiente al año
# 2014 e imprima por pantalla el número de días que han pasado desde el 1 de
# Enero de 2014 hasta la fecha dada.

dia = int(input("Escriba el dia: "))
mes = int(input("Escriba el mes:" ))
año = 2014
f1 = datetime.date(año,mes,dia)
f2 = datetime.date(2014,1,1)
diferencia = f1 - f2

print("El número de días que han pasado desde el 1 de Enero de 2014 son: {} dias.".format(diferencia.days))
