from random import shuffle

string = input("Введите предложение:  ")
string = string.lower()
string = string.replace("."," ")
string = string.replace(","," ")
L = string.split()
shuffle(L)
l = " ".join(L)
print(l[0].upper() + l[1:] + ".")  