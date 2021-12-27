from math import sqrt
#Dados tres (3) números, Hacer una aplicación que calcule la resolvente.
A = int(input("Ingrese el coeficiente de la variable cuadrática: "))
B = int(input("Ingrese el coeficiente de la variable lineal: "))
C = int(input("Ingrese el término independiente: "))
if ((B**2)-4*A*C) < 0:
      print("La solución de la ecuación es con numeros complejos")
else:
  x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)  # Fórmula de Bhaskara parte positiva
  x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)  # Fórmula de Bhaskara parte negativa
  print("Las soluciones de la ecuación son:")
  print(x1)
  print(x2)