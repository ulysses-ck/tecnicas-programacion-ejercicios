# Este es un programa que permite que el usuario
# ingrese el total de una compra y restar el descuento correspondiente

# montoTotal, descuento, montoFinal son reales

descuento = 0.15
montoTotal = float(input())
# se convierte montoTotal a tipo float(punto flotante, real)
# para evitar error de operación con enteros y reales

montoFinal = montoTotal - montoTotal * descuento
print(montoFinal)