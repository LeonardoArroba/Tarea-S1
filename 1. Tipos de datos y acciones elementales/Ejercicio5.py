import math
#Dados dos (2) lados de un triángulo en cm, calcular la hipotenusa del mismo.
a=float(input("ingrese un cateto\n"))
b=float(input("ingrese el otro cateto\n"))
c=math.sqrt((a*a+b*b))
print(str(c))
