for i in range(11,10000001):
	n = str(i)
	r = n[1 : :] + n[0]
	
	div = int(r)/i
	if div == 3.5:
		print("i",i,"r",r) 
	
	