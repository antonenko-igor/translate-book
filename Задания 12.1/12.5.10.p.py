words = [line.strip() for line in open('wordlist.txt')]

for word in words:
	vowels = "aeiou"
	count = 0
	max_count = 0

	for i in range(len(word)):
		if word[i] in vowels:
			count += 1
			max_count = max(max_count, count)
		else:
			count = 0
	if max_count >= 4:
		print(word) 








	

	
		