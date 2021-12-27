# Dados tres números enteros positivos A, B y C, determine ¿cuál de ellos es el
# mayor? y ¿cuál es el segundo mayor?

A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))
C = int(input("Ingrese el valor de C: "))

#Primer Mayor
if B < A > C:
    print("El numero mayor es el primer numero. Numero: " + str(A))
elif A < B > C:
    print("El numero mayor es el segundo numero. Numero: " + str(B))  
elif A < C > B:
    print("El numero mayor es el tercer numero. Numero: " + str(C))
       
else:
    print("Todos los numeros son iguales")

#Segundo Mayor
if B < A < C:
        print("El segundo mayor es el primer numero. Numero: " + str(A))
elif A > B > C:
        print("El segundo mayor es el segundo numero. Numero: " + str(B))
elif A > C < B:
        print("El segundo mayor es el tercer numero. Numero: " + str(C))
else:
    print("Todos los numeros son iguales")