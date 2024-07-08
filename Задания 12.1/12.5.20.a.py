emails = [line.strip() for line in open('emailslist.txt')]

for email in emails:
	print(email, end = "; ")  