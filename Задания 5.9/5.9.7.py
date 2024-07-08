from math import sqrt

num = eval(input("Введите целое число:  "))
flag = 0
for i in range(2,num + 1):
	if num % i == 0:
		print(i,end = "  ")
		y = i
		if y % sqrt(y) == 0:
			flag = 1
print()			
if flag == 1:
	print(num,"Число квадратное.")
else:
	print(num,"Число бесквадратное.") 


		
		
		
		
