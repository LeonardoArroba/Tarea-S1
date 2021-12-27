# El IMC resulta de la división de la masa del individuo (en kilogramos) entre el
# cuadrado de la estatura (en metros). El índice de masa corporal es un indicador
# del peso de una persona en relación con su altura.
# Clasificación del IMC de acuerdo con la OMS de la ONU:
# a. Menor a 16: Criterio de ingreso.
# b. 16 a 16.9: infra peso.
# c. 17 a 18.4: bajo peso.
# d. 18.5 a 24.9: peso normal.
# e. 25 a 29.9: sobrepeso.
# f. 30 a 34.9: obesidad pre-mórbida.
# g. 40 a 45: obesidad mórbida.
# h. Mayor a 45: obesidad híper-mórbida.
# Dado el peso de una persona en libras (1 libra = 0,453592 Kg) y su estatura en
# centímetros, calcule su IMC e indique como salida el peso en kilogramos, el valor
# de IMC de la persona y la categoría en la cual fue clasificado.

peso = float(input("Escriba su peso(kg): "))
estatura = float(input("Escriba su estatura(m): "))
imc = peso / (estatura ** 2)

if 16 <= imc and imc < 16.9:
    print("Su IMC es de: {}.Su categoria es: Infra Peso.".format(imc))
elif 17 <= imc and imc < 18.4:
    print("Su IMC es de: {}. Su categoria es: Bajo Peso.".format(imc))
elif 18.5 <= imc and imc < 24.9:
    print("Su IMC es de: {}. Su categoria es: Peso Normal.".format(imc))
elif 25 <= imc and imc < 29.9:
    print("Su IMC es de: {}. Su categoria es: Sobrepeso.".format(imc))
elif 30 <= imc and imc < 34.9:
    print("Su IMC es de: {}. Su categoria es: Obesidad Pre-morbida.".format(imc))
elif 40 <= imc and imc < 45:
    print("Su IMC es de: {}. Su categoria es: Obesidad Morbida.".format(imc))
else:
    print("Obesidad Hiper-morbida") 
    