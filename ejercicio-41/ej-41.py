km_recorridos = 0
total_kcal = 0
for i in range(4):
	kilometros = input()
	km_recorridos += int(kilometros)
	total_kcal += int(kilometros) // 2 * 380
promedio = km_recorridos / 4
print(km_recorridos)
print(promedio)
print(total_kcal)
