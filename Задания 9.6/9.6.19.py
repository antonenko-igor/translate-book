from random import randint

for _ in range(9):
    L = []
    for _ in range(9):    	
    	e = randint(1,9)
    	while L.count(e)!=0:
    		e = randint(1,9)
    	L.append(e)
    	print(e, end=" ")       
    print() 

		
	

	
		
	
	

	
	
	
	
	
	


		
	