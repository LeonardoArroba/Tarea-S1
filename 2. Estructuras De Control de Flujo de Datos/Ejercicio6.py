# En un estacionamiento el monto a pagar se calcula multiplicando el número de
# horas que permaneció el automóvil dentro del estacionamiento por Bs. 4 y se
# incrementa esta cantidad en Bs. 2,50 por cada media hora adicional.
# Ahora se desea que usted elabore un algoritmo que a partir de la hora de entrada
# y la hora de salida de un vehículo (las mismas corresponden a un mismo día)
# calcule el monto a pagar por el dueño del vehículo.
# La entrada vendrá dada por dos enteros positivos el primero representa las horas
# y el segundo los minutos, además por último se debe leer un carácter (A o P) que
# indica si la hora es AM o PM.

pago_hora = 4
mediah_adi = 2.5

while True:
    horas = int(input("Cantidad de horas que permanecio en el estacionamiento: "))
    minutos = int(input("Cantidad de minutos que permanecio en el estacionamiento: "))
    if minutos > 0:
        horas += mediah_adi
    pago_total = horas * pago_hora
    print("Total a pagar por {} horas es: {}".format(horas,pago_total)) 
    otro = input("Desea hacer otro claculo ")
    if otro == "n" or otro == "N":
        break