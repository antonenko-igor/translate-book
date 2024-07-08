lines = [line.strip() for line in open("logfile.txt")]
print(lines)
for line in lines:	
	L = line.split(",")
	#print(L[1][:3],L[1][4:6], L[2][:3],L[2][4:6])
	if int(L[2][4:6]) < int(L[1][4:6]):
		h = int(L[2][:3]) - int(L[1][:3]) - 1
		m = str((int(L[2][4:6]) - int(L[1][4:6]))%60)
		if h >= 1:
			print(L[0],str(h),":",m)
		
	else:
		h = int(L[2][:3]) - int(L[1][:3])
		m = str((int(L[2][4:6]) - int(L[1][4:6]))%60)
		if h >= 1:
			print(L[0],str(h),":",m) 
		

	