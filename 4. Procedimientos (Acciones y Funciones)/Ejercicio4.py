# En una empresa pagan según las horas trabajadas y una tarifa fija por hora. Si la
# cantidad de horas trabajadas en una semana es mayor a 40, la tarifa se
# incrementa en un 35% para las horas extras. Escribe una acción principal que
# solicite la identificación de 5 empleados, el monto cancelado por hora, y la
# cantidad de horas trabajadas por cada uno, llame a acciones/funciones que
# calculen el salario semanal por horas trabajadas (<=40) y los ingresos por
# concepto de horas extras, y finalmente informe los resultados en la acción
# principal.

def salario():
    nombre = input("Ingrese el nombre del empleado: ")
    pago = int(input("Ingrese monto a calcelar por hora: "))
    horas = int(input("Ingrese la cantidad de horas trabajadas: "))
    
    nombre1 = input("Ingrese el nombre del empleado: ")
    pago1 = int(input("Ingrese monto a calcelar por hora: "))
    horas1 = int(input("Ingrese la cantidad de horas trabajadas: "))
    
    nombre2 = input("Ingrese el nombre del empleado: ")
    pago2 = int(input("Ingrese monto a calcelar por hora: "))
    horas2 = int(input("Ingrese la cantidad de horas trabajadas: "))
    
    nombre3 = input("Ingrese el nombre del empleado: ")
    pago3 = int(input("Ingrese monto a calcelar por hora: "))
    horas3 = int(input("Ingrese la cantidad de horas trabajadas: "))
    
    nombre4 = input("Ingrese el nombre del empleado: ")
    pago4 = int(input("Ingrese monto a calcelar por hora: "))
    horas4 = int(input("Ingrese la cantidad de horas trabajadas: "))
    if horas > 40:
        horasExtras = horas - 40
        sueldo = (40 * pago) + (horasExtras * (pago * 1.35))
        print("Horas extras trabajadas es: {}".format(horasExtras))
        print("El sueldo extra es: ${}".format(int(horasExtras * (pago * 1.35))))
        print("El sueldo total de {} es: ${}".format(nombre,sueldo))
    if horas1 > 40:
        horasExtras1 = horas1 - 40
        sueldo1 = (40 * pago1) + (horasExtras1 * (pago1 * 1.35))
        print("Horas extras trabajadas es: {}".format(horasExtras1))
        print("El sueldo extra es: ${}".format(int(horasExtras1 * (pago * 1.35))))
        print("El sueldo total de {} es: ${}".format(nombre1,sueldo1))
    if horas2 > 40:
        horasExtras2 = horas2 - 40
        sueldo2 = (40 * pago2) + (horasExtras2 * (pago2 * 1.35))
        print("Horas extras trabajadas es: {}".format(horasExtras2))
        print("El sueldo extra es: ${}".format(int(horasExtras2 * (pago * 1.35))))
        print("El sueldo total de {} es: ${}".format(nombre2,sueldo2))
    if horas3 > 40:
        horasExtras3 = horas3 - 40
        sueldo3 = (40 * pago3) + (horasExtras3 * (pago3 * 1.35))
        print("Horas extras trabajadas es: {}".format(horasExtras3))
        print("El sueldo extra es: ${}".format(int(horasExtras3 * (pago * 1.35))))
        print("El sueldo total de {} es: ${}".format(nombre3,sueldo3))
    if horas4 > 40:
        horasExtras4 = horas4 - 40
        sueldo4 = (40 * pago4) + (horasExtras4 * (pago4 * 1.35))
        print("Horas extras trabajadas es: {}".format(horasExtras4))
        print("El sueldo extra es: ${}".format(int(horasExtras4 * (pago * 1.35))))
        print("El sueldo total de {} es: ${}".format(nombre4,sueldo4))
    else:
        sueldo = horas * pago
        print("El sueldo de {} por {} horas es: ${}".format(nombre,horas,sueldo))
        sueldo1 = horas1 * pago1
        print("El sueldo de {} por {} horas es: ${}".format(nombre1,horas1,sueldo1))
        sueldo2 = horas2 * pago2
        print("El sueldo de {} por {} horas es: ${}".format(nombre2,horas2,sueldo2))
        sueldo3 = horas3 * pago3
        print("El sueldo de {} por {} horas es: ${}".format(nombre3,horas3,sueldo3))
        sueldo4 = horas4 * pago4
        print("El sueldo de {} por {} horas es: ${}".format(nombre4,horas4,sueldo4))
        
salario()