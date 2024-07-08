board = [[0, "M", 0, "M", 0],
         [0,  0, "M", 0,  0],
         [0,  0,  0,  0,  0],
         ["M","M",0,  0,  0],
         [0,  0,  0, "M", 0]]

new_board = [["0" for _ in range(5)] for _ in range(5)]


for row in range(5):
	for col in range(5):
		if board[row][col] == "M":
			new_board[row][col] = "M"
		else:
			c = 0
			for i in range(max(0,row - 1),min(5,row + 2)):
				for j in range(max(0,col - 1), min(5,col + 2)):
					if board[i][j] == "M":
						c += 1
			new_board[row][col] = " " +str(c) 

for r in new_board:
	print("   ".join(r)) 