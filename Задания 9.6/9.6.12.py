from random import randint

L = [randint(0,10) for _ in range(7)]
print(L)

n = 0
while True:
	for i in range(len(L)):
		if L[i] > 0:
			L[i] = 1
			n = 1
			print(L)
			break
	break			
if n == 0:
	print("Ненулевых значений не имеется.")  
			    


