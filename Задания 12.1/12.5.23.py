from random import choice
acronym = input("Введите акроним(английские буквы):  ")
words = [line.strip() for line in open('wordlist.txt')]
A = []
for i in range(len(acronym)):
	L = []
	for word in words:	
		if word[0] == acronym[i].lower():
			L.append(word)
	A.append(choice(L))	    
print(A) 

	