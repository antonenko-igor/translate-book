words = [line.strip() for line in open('wordlist.txt')]

letters = input("Введите буквы:  ")

for word in words:
	if len(word) >= len(letters):
		while True:
			for letter in word:
				if letter not in letters:
					break
			else:
				for letter in letters:
					if letter not in word:
						break
				else:
					print(word)				
			break 





			



			
		
			
			
	
	
		
			
		
			
	
			
	
			
		
	



