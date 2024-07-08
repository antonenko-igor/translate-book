from random import choice
class Rock_paper_scissors():
	def __init__(self,rounds = 5):
		self.rounds = rounds
		self.current_round = 0
		self.player_wins = 0
		self.computer_wins = 0

	def computer_choice(self):
		choices = ["бумага", "камень", "ножницы"]
		return choice(choices)

	def find_winner(self,player_choice, computer_choice):
		if player_choice == computer_choice:
			return f"Ничья"
		elif (player_choice == "камень" and computer_choice == "ножницы") \
		      or (player_choice == "бумага" and computer_choice == "камень") \
		      or (player_choice == "ножницы" and computer_choice == "бумага"):
			self.player_wins += 1
			return f"Игрок выиграл этот раунд."
		else:
			self.computer_wins += 1
			return f"Компьютер выиграл этот раунд."

	def check_game_winner(self):
		if self.player_wins == self.computer_wins:
			return f"Ничья!"
		elif self.player_wins > self.computer_wins:
			return f"Игрок выиграл игру!"
		else:
			return f"Компьютер выиграл игру!"

	def play_round(self,player_choice):
		self.current_round += 1
		computer_choice = self.computer_choice()
		print(f"Раунд {self.current_round}: Выбор игрока - {player_choice},\
			Выбор компьютера - {computer_choice}")

		result = self.find_winner(player_choice, computer_choice)
		print(result)

		if self.current_round == self.rounds:
			game_winner = self.check_game_winner()
			print(game_winner)        	        
game = Rock_paper_scissors(3)
while game.current_round < game.rounds:
	player_choice = input("Ваш выбор из (бумага, камень, ножницы) - ")
	game.play_round(player_choice) 
	

