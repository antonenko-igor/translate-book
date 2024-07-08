class Investment:
	def __init__(self,principal,interest):
		self.principal = principal
		self.interest = interest
		
	def __str__(self):
		return ("Principal - ${:d},Interest rate - {:.2f}%".format(self.principal,
			    self.interest))

	def value_after(self,n):
		return self.principal*(1 + self.interest)**n
    	                   
investment = Investment(1000,5.12)
print(investment)
print(investment.value_after(5)) 
