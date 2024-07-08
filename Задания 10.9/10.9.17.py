L = []
print("Для окончания ввода нажмите - готов")
while True:
	h = input("Введите высоту в формате(футы'дюймы''):  ")
	if h == "готов":
		break
	x = h.split("'")
	k = x[0]
	n = int(x[0]) + float("{:.2f}".format(int(x[1])*(1/12)))
	L.append(n)
for i in range(4,13):
	count = 0
	for j in L:
		if int(j) == i:
			count +=1
	print(i,"-футовых = ",count) 



