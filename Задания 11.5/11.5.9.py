from random import randint
values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
deck = []
for s in suits:
    for v in values:
        deck.append((v,s))

#print(len(deck))
L = []
for i in range(3):
    L.append(deck[randint(1,53)])
print(L)
print(L[1][1])
