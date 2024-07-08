def is_sudoku_valid(sudoku):
	for i in range(9):
		if sum(sudoku[i]) != 45:
			return False
	for j in range(9):
		if sum([sudoku[i][j] for i in range(9)]) != 45:
			return False
	for i in range(0,9,3):
		for j in range(0,9,3):
			if sum([sudoku[x][y] for x in range(i,i+3) for y in range(j,j+3)]) != 45:
				return False
	return True

right_sudoku = [[8,3,9,4,2,6,7,5,1],
               [4,7,5,3,1,8,6,9,2],
               [1,6,2,7,5,9,3,4,8],
               [9,1,3,2,7,4,5,8,6],
               [5,2,4,6,8,3,1,7,9],
               [7,8,6,1,9,5,4,2,3],
               [2,5,7,9,6,1,8,3,4],
               [6,4,8,5,3,2,9,1,7],
               [3,9,1,8,4,7,2,6,5]]

wrong_sudoku = [[8,3,9,4,2,6,7,5,1],
               [4,7,5,3,1,8,6,9,2],
               [1,6,2,7,5,9,3,4,8],
               [9,1,3,2,7,4,5,8,6],
               [5,2,4,6,8,3,1,7,9],
               [7,8,6,1,9,5,4,2,3],
               [2,5,7,9,6,1,8,3,4],
               [6,4,8,5,3,2,9,1,7],
               [3,9,1,8,4,7,2,6,7]]
print(is_sudoku_valid(right_sudoku))
print(is_sudoku_valid(wrong_sudoku)) 