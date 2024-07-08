from random import sample

user_numbers = sample(range(1,11),6)
user_numbers.sort()

total_count = 0
for _ in range(1000):
	winning_numbers = sample(range(1,11),6)
	winning_numbers.sort()
	count = 1

	while user_numbers != winning_numbers:
		winning_numbers = sample(range(1,11),6)
		winning_numbers.sort()
		count += 1

	total_count += count
	average_count = total_count/1000

print("Среднее число  при совпадении для 1000 попыток  - ", round(average_count,2)) 