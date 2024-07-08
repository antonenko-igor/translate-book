num = eval(input("Введите целое число:  "))

N = []
for i in range(1,num + 1):
	if num % i == 0:
		N.append(i)
print("Делители введённого числа ", N)		