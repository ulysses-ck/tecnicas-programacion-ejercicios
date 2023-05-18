categoria = input()
cantidad_dias = int(input())

if (categoria == "pediatria"):
	resultado = 3500 * cantidad_dias
elif (categoria == "maternidad"):
	resultado = 2500 * cantidad_dias
else:
	resultado = 3000 * cantidad_dias

print(resultado)