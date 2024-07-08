words = [line.strip() for line in open('wordlist.txt')]

c = 0
for word in words:
	if "r" in word or "s" in word or "t" in word or "l" in word or "n" \
	   in word or "e" in word:
		c += 1
print(c)  

 