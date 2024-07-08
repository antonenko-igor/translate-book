num = eval(input("Введите десятичную высоту в футах:  "))
d_num = int(num)
f_num = num - d_num
print("Футов - ",d_num,",","дюймов" , "{:.2f}".format(f_num*12) ) 