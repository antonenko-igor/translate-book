from math import log

count = 0
n = eval(input("Введите значение n: "))
for i in range(2,(n+1)):
	    count = count + (1/i)        
print("Для", n,"  ",(1 + count) - log(n))	
