string = input("Введите строку для шифрования:  ")
block = eval(input("На сколько частей разбивать: "))
encrypted = ""
for i in range(block):
    for j in range(i,len(string),block):
        encrypted +=  string[j]
print(encrypted) 
        
