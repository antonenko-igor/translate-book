def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return True
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return True

    if board[0][0] == board[1][1] == board[2][2] != 0:
        return True
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return True

    return False

print(check_winner([[1,0,2],[0,1,0],[2,2,1]])) 