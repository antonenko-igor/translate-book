L = []
for i in range(11,10001):
	n = str(i)
	ad = 0
	mul = 1	
	for j in range(len(n)):
		ad = ad + int(n[j])
		mul = mul * int(n[j])
		add = ad + mul
	if i == add:
		L.append(add)
print(L) 


			
			


	


 