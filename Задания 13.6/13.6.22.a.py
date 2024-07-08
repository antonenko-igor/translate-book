import random

def chose_2(board):
	spots_0 = []
	for i in range(3):
		for j in range(3):
			if board[i][j] == 0:
				spots_0.append((i,j))

	if spots_0:
		choice = random.choice(spots_0)
		board[choice[0]][choice[1]] = 2
	return board


print(chose_2([[1,0,2],[0,1,0],[2,2,1]])) 
