width = eval(input("Введите ширину: "))
height = eval(input("Ведите высоту: "))
count = 0
for i in range(height):
    for j in range(width):
        print(count % 10, end="  ")
        count = count + 1
    print(end="\n") 