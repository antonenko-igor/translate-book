from random import shuffle

string = input("Введите предложение:  ")
L = string.split()
shuffle(L)
print(" ".join(L)) 