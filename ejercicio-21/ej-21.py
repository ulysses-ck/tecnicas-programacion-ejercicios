medio_de_pago = input()
monto = input()

if(monto > 5000 and medio_de_pago == "efectivo"):
	resultado = monto - monto * 0.15
elif(monto > 2000):
    resultado = monto - monto * 0.1
else:
    print(monto)
print(resultado)