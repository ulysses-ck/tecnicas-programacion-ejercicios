# 37. Se requiere de un algoritmo que permita ingresar los registros de un censo hasta que el censista indique
# que ya ha cargado todos los resultados. Cuando esto ocurra, se deberá informar cantidad de personas
# censadas, el promedio de edad de ellos y cuantas de estas personas cuentan con internet en sus hogares.
# DF – PS - PY
contador_persona = 0
suma = 0
contador_internet = 0

while True:
	edad = input("¿Cual es su edad? Escribir un numero negativo para detener el censo\n")
	if int(edad) < 0:
		break
	tiene_internet = input("¿Cuenta con conexión a internet? Responder con 'si' o 'no'\n")


	suma += int(edad)
	contador_persona += 1
	if tiene_internet == "si":
		contador_internet += 1

promedio = suma / contador_persona

print(contador_persona)
print(promedio)
print(f"De {contador_persona} personas, {contador_internet} poseen conexion a internet")
