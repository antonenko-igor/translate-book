L = []
n = ["0","1","6","8","9"]
for i in range(10, 100000):
	a = str(i)
	flag = 0
	for j in range(len(a)):
		if a[j] not in n:
			flag = 1
	if flag == 0:
		L.append(a)

M = []
for n in L:
	x = n 
	y = x[::-1]
	z = ""
	for i in range(len(y)):
		if y[i] == "6":
			z += "9"
		elif y[i] == "9":
			z += "6"
		else:
			z += y[i]
	if x == z:
		M.append(int(z))
print(M) 




				
			
				