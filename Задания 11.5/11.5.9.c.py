from random import randint,shuffle
deck = [{'value':i, 'suit':c}
for c in ["трефы","пики","бубны","червы"]
for i in range(2,15)]
shuffle(deck)
#print(deck)

L = []
for i in range(3):
	L.append(deck[randint(0,51)]["value"])
#print(L)
if L.count(L[0]) == 2 or L.count(L[2]) == 2:
	print("Пара ")

else:
	print("Нет пары") 