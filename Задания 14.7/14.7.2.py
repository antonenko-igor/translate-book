class Product:
	def __init__(self,name,amount,price):
		self.name = n
		self.amount = a
		self.price = p 

	def get_price(self):
		return f"Обычная цена - {round(self.amount * self.price, 2)}"

	def make_purchase(self):
		if self.amount < 10:
			return f"Цена со скидкой - {round(a*p, 2)}"

		if self.amount >= 10 and self.amount < 100:
			return f"Цена со скидкой - {round(a * p - (int(a*p*10/100)), 2)}"

		if self.amount > 100:
			return f"Обычная цена - {round(a*p - (a*p*20/100), 2)}"

n = input("Наименование товара : ")
a = eval(input("Количество товара : "))
p = eval(input("Стоимость товара : "))

c = Product(n,a,p)
print(c.get_price())
print(c.make_purchase()) 
