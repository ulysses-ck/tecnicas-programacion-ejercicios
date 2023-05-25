valor_entrada = input()

while(True):
	edad = input()

	if edad < 0:
		break

	if edad < 45:
		if edad < 25:
			if edad < 15:
				descuento = valor_entrada * 0.35
			else:
				descuento = valor_entrada * 0.25
		else:
			descuento = valor_entrada * 0.2
	else:
		descuento = valor_entrada * 0.15

print(descuento)
