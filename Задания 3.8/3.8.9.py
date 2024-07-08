hour = eval(input("Введите час между 1 и 12: "))
x = eval(input("Сколько часов вперед?: "))
print("Новый час: ",(hour + x)%12) 