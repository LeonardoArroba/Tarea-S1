# En un almacén se hace un 20% de descuento a los clientes cuya compra supere
# los Bs 1000, se desea que realice un algoritmo el cual tome por entrada el monto a
# pagar por el cliente y arroje como salida el monto aplicando el descuento de ser
# necesario.

pago = int(input("Ingrese el valor a pagar: "))
des = 0.20
if pago > 1000:
    descuento = des * pago
    totalApagar = pago - descuento
    print("El monto aplicando el descuesto es de: Bs {}".format(totalApagar))
else: 
    print("No aplica para el descuento")
    