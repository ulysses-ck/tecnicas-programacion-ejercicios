suma_sueldos = 0
suma_comisiones = 0
while True:
	sueldo = int(
	    input(
	        "Ingrese el monto del sueldo. Escriba un numero negativo para finalizar el ingreso"
	    ))

	if sueldo < 0:
		break
	suma_sueldos += sueldo
	if sueldo > 50000:
		comision = sueldo * 0.1
	else:
		comision = sueldo * 0.15
	suma_comisiones += comision
	print(f"El sueldo más el aumento correspondiente es: {sueldo + comision}")
print(suma_sueldos)
print(suma_comisiones)
