s = input("Enter a word")
words = [line.strip() for line in open('wordlist.txt')]
for word in words:
	count = 0
	if word < s:
		for i in word:
			if i in s :
				count += 1
		if len(word) == count:
			print(word) 
			

				