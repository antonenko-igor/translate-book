words = [line.strip() for line in open('wordlist.txt')]
for word in words:
	count = 0
	for i in range(len(word)):
		if word[i:i+2] == "ab":
			count +=1
	if count >= 2:
		print(word)
print()
# Другое решение
for word in words:
	if word.count("ab") >= 2:
		print(word)  
