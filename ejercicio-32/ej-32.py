contador = 0
suma = 0
menor = 999
mayor = -999

while(True):
	numero = int(input())

	if(numero == 0 or numero < 0):
		break
	contador+=1
	suma += numero

	if(numero < menor):
		menor = numero
	elif(numero > mayor):
		mayor = numero

print(contador)
print(suma)
print(menor)
print(mayor)