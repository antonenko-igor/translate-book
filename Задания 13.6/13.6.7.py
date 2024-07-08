from random import randint

def ran_int(n):
	
	while True:
		x = ""
		for i in range(n):
			x += str(randint(0,9))
		if x[0] != "0":
			break
	return x
print(ran_int(3)) 
	