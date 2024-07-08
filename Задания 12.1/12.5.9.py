lines = [line.strip() for line in open('expenses.txt')]

for i in range(1,10):
	count = 0
	for line in lines:
		if int(line[0]) == i:
			count +=1
	print("Для ",i," - ",(count/len(lines))*100,"%")
	print()  
    
	
