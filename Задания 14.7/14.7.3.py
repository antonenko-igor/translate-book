class Password_manager:
	def __init__(self):
		self.old_passwords = [] 
		
	def get_password(self):
		return self.old_passwords[-1]

	def set_passwords(self,new_pass):
		if new_pass in self.old_passwords:
			return f"Пароль имеется в списке. Введите новый пароль."
		else:
			self.old_passwords.append(new_pass)
			return f"Новый пароль установлен."
		

	def is_correct(self, your_password):
		if your_password == self.old_passwords[-1]:
			return True
		else:
			return False

a = Password_manager()
print(a.set_passwords("password123")) #Вывод - Новый пароль установлен.
print(a.set_passwords("password123")) #Вывод - Пароль имеется в списке. 
                                      #Введите новый пароль.
print(a.get_password()) #Вывод - password123
print(a.is_correct("password123")) #Вывод - True
print(a.is_correct("password")) #Вывод - False 

