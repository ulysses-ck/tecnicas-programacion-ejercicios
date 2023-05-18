monto_hora = int(input())
horas_trabajo = int(input())
if (horas_trabajo > 160):
	horas_extras = horas_trabajo - 160
	sueldo_neto = (horas_trabajo - horas_extras) * monto_hora
	sueldo_horas_extras = horas_extras * (monto_hora * 2)
	sueldo_total = sueldo_horas_extras + sueldo_neto
	print(sueldo_total)
else:
	sueldo_neto = horas_trabajo * monto_hora
	print(sueldo_neto)