# written by Antonenko Igor

"""
Правильность вывода зависить от того, где будет запущена программа.
IDLE Shell 3.11.4 выдает неправильный результат. 
Рекомендуется запускать в py.exe или командной строке.
"""
height = eval(input("Введите высоту  буквы А: "))
print(" "*(height)+" * ")
for i in range(int(height/1.4)-1):
	print(" "*(height-i)+"*" +" "*(i*2)+ " *", )
print(" "*((height-i)-1)+ "*"*5+"*"*(i*2))
for i in range(int((height/1.4)-1) + 1, height-1):
	print(" "*(height-i)+"*" +" "*(i*2)+ " *",)

input() 
