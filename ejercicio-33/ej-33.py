notas_mayores = 0
notas_menores = 0

for i in range(0,10):
	nota = int(input())
	if(nota >= 7):
		notas_mayores += 1
	else:
		notas_menores += 1
print(notas_menores)
print(notas_mayores)