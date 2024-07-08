from random import randint
M = []
print("Количество бросков кубиков - 1000 раз")
for i in range(1000):
	L = []	 
	for i in range(4):
		r = randint(1,6)
		L.append(r)	
	M.append(L[0]+L[1])
	M.append(L[0]+L[2])
	M.append(L[0]+L[3])
	M.append(L[1]+L[2])
	M.append(L[1]+L[3])
	M.append(L[2]+L[3])
for k in range(2,13):
	print("для суммы - ", k," выпадений - ",M.count(k),
		  " -- {:.1f}".format((M.count(k)/1000)*100),"%")
	print()  
