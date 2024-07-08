# "11 - валет, 12 - дама, 13 - король, 14 - туз"
from random import shuffle, randint
suits = ["трефы","пики","бубны","червы"]
deck = []
deck = [{'value':i, 'suit':c}
for c in suits
for i in range(2,15)]
shuffle(deck)
player1 = []
player2 = []

while True:
    for i in range(3):
        player1.append(deck[randint(2,15)]["value"])
    for i in range(3):
        player2.append(deck[randint(2,15)]["value"])        
    player1.sort()
    player2.sort() 

    if player1 == player2:
        print("Ничья")
        break    
    if player1[2] > player2[2]:
        print("Игрок1 победил. Счет равен",player1[2]," > ",player2[2])
        break
    if player1[2] < player2[2]:
        print("Игрок2 победил.Счет равен",player1[2]," < ",player2[2])
        break    
    if player1[2] == player2[2]:
        if player1[1] > player2[1]:
            print("Игрок1 победил. Счет равен",player1[1]," > ",player2[1])
            break       
        if player1[1] < player2[1]:
            print("Игрок2 победил.Счет равен",player1[1]," < ",player2[1])
            break
            
    if player1[1] == player2[1]:
        if player1[0] > player2[0]:
            print("Игрок1 победил. Счет равен",player1[0]," > ",player2[0])
            break
        else:
            print("Игрок2 победил.Счет равен",player1[0]," < ",player2[0])
            break