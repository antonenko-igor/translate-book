# Igor Antonenko

from random import randint

win_no_change = 0
win_change = 0

for _ in range(10000):
  car = randint(1,3)
  player = randint(1,3)
  # no change
  if player == car:
    win_no_change = win_no_change + 1
  # change
  elif player != car:
    win_change = win_change + 1
print("Без выбора другой двери - ",round((win_no_change/10000)*100, 2),"%")
print("С выбором другой двери - ", round((win_change/10000)*100, 2),"%") 