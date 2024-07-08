L = []
for v in range(1,100):	
	for x in range(0,100):
		for y in range(0,100):			
				if 7*x + 11*y == v:
					L.append(v)
M = []
for i in range(100):
	if i not in L:
		M.append(i)
print("Наибольшая цена покупки, которую нельзя оплатить - ",max(M), "центов.") 
