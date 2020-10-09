print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = int(input("a = "))
b = int(input("b = "))
c = 0
while c < 10:
	discr = b ** 2 - 4 * a * c
	if discr <= 0:
		print('Результат меньше 0, корней нет')
	elif discr == 0:
		print('Результат равен 0, корней нет')
	else:
		print('Идет подсчет...')
	c = c + 1
	print('c =', c)
	print("Дискриминант D = %.2f" % discr)

for c  in range(10):
	discr = b ** 2 - 4 * a * c
	if discr <= 0:
		print('Результат меньше 0, корней нет')
	elif discr == 0:
		print('Результат равен 0, корней нет')
	else:
		print('Идет подсчет...')
	print('c =', c)
	print("Дискриминант D = %.2f" % discr)

