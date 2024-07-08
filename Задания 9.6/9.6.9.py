num = eval(input("Введите число:  "))
a = 1
d = 1
b = num
while d >= 0.00000000001:
	n =(a+(num/a))/2
	a = n
	d = b - n
	b = n
print("Квадратный корень числа ",num,"равен " ,n) 
    

     
    
	
	
	
	
	
    
