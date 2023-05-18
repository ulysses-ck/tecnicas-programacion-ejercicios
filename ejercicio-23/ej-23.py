kw_mes = float(input())

if (kw_mes > 200):
	resultado = 30 * 6.03 + 90 * 6.19 + 80 * 6.78 + (kw_mes - 200) * 7.24
else:
	resultado = 30 * 6.03 + 90 * 6.19 + (kw_mes - 120) * 6.78
print(resultado)
