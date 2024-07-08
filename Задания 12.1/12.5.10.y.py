
words = [line.strip() for line in open('wordlist.txt')]

vowels = "aeiou"

for let_first in "bcdfghjklmnpqrstvwxyz":
	for let_last in "bcdfghjklmnpqrstvwxyz":
		L = []
		for vovel in vowels:
			if (let_first + vovel + let_last)   in words:
				L.append(let_first + vovel + let_last)				
			else:
				break
		if len(L) == 5:
			print(" ".join(L)) 

		
				
		
		

				
			
				
			 
		
	
			



		    
			
				
					
			
			

	
			
				
				
					
			    
			    	

					
		
					 
			   
			