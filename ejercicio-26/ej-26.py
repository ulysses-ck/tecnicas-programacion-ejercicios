nombre_articulo = input("a. Nombre del Artículo.")
precio = float(input("b. Precio o costo unitario."))
numero_departamento = input(
    "c. Número de departamento en donde se localiza el producto.")

if (numero_departamento == 1):
	resultado = precio * 0.1
elif (numero_departamento == 2):
	resultado = precio * 0.15
elif (numero_departamento == 3):
	resultado = precio * 0.2
else:
	resultado = precio * 0.05

print(f"El precio final del {nombre_articulo} es: ", resultado)
