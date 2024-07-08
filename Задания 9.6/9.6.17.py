numerator = int(input("Введите числитель: "))
denominator = int(input("Введите знаменатель: "))
digit_position = int(input("Введите  позицию искомой цифры: "))

decimal = numerator / denominator

digit = int(decimal * 10**digit_position) % 10
print("Цифра с позицией ", digit_position, "равна:", digit) 