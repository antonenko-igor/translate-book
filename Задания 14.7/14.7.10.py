class Connect4:
	def __init__(self):
		self.board = [[' ' for _ in range(7)] for _ in range(6)]
		self.players = ['X', 'O']
		self.player = 0


	def print_board(self):
	 	for row in self.board:
	 		print("  |  ".join(row) + "  |")
	 		print("-" * 34)
	 	print("    ".join([str(i) for i in range(7)]))
	 	print()
	    
    	
    		
	def get_spots(self, col):
		if 0 <= col < 7 and self.board[0][col] == ' ':
			for i in range(5, -1, -1):
				if self.board[i][col] == ' ':
					self.board[i][col] = self.players[self.player]
					return True
		return False


	



game = Connect4()
game.print_board()
game.get_spots(0)
input()
