words = [line.strip() for line in open('wordlist.txt')]

for word in words:
	if len(word) >= 8:
		start = list(word[:4])
		end = list(word[-4:])
		start.sort()
		end.sort()
		if start == end:
			print(word) 
	
	
	
	

	
		


	
		
		
			
		

			
		
	
	