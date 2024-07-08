from random import choice
L = ["слово","буква","программа","разница","семь","значение",
    "правильно","корень","список","догадка"]
c = 0

while c != 1:
	word = choice(L)	
	for i in range(len(word)):
		c = word.count(word[i])
		if c == 2:
			break					
print(word)	

		


    