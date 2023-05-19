suma_edad = 0
contador = 0

while(True):
	edad = input()
	if(edad == "detener"):
		break
	suma_edad+=edad
	contador+=1

print(suma_edad)
print(contador)
