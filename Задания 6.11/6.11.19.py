num = input("Введите большое целое число:  ")
numreverse = (n[: :-1])
c = 0
s = " "
for i in range(len(nreverse)):
	c = c + 1
	if c % 3 == 0:
		s = s + numreverse[i] + ","
	else:
		s  = s + numreverse[i]
num = s[: :-1]    	    
if num[0] == ",":
	print(num[1:])
else:
	print(num) 

	
		
		
	
