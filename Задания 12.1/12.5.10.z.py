words = [line.strip() for line in open('wordlist.txt')]
largest = ""
x = 0
for word in words:
	c = 0
	for i in range(len(word)):
		if word[i] == "i":
			c += 1
	if c>x:
		x = c 
		largest = word
print(largest) 

				

