venta_refacciones = input("Ingrese importe de venta de facciones")
venta_servicios = input("Ingrese importe de venta de servicios")
venta_auto_camiones = input("Ingrese importe de venta de autos y camiones")

resultado = (venta_refacciones + venta_servicios + venta_auto_camiones) / 3

if(resultado>= 50000):
	print("Se alcanzo el objetivo")
else:
	print("Buscar nuevas estrategias de ventas")
