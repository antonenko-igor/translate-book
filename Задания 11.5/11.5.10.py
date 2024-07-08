from random import randint,shuffle
deck = [{'value':i, 'suit':c}
for c in ["трефы","пики","бубны","червы"]
for i in range(2,15)]
shuffle(deck)

count = 0
for _ in range(100000):
	L = []
	for i in range(5):
		L.append(deck[randint(0,51)]["suit"])
		if L.count(L[0]) == 5:
			count += 1
print("Вероятность флеша из 5 карт составляет - ",(count/100000)*100, "%") 





	
	
	
	

	
	
	

