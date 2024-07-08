lines = [line.strip() for line in open("namelist.txt")]

L = ["a","e","i","o",'u']
for line in lines:
	M = []	
	for i in range(len(line)):
		k = line[i].lower()
		if k in L:
			if k not in M:
				M.append(k)			   
	if M == L:
		print(line) 
	
	
	
	
	

		
			
