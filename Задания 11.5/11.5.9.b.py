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
if L[0] == L[1] == L[2]:
	print("Три подряд",L[0])
else:
	print("Нет") 
