def backtracking_nqueen(board, row):
	if row == N:
		return True
	for col in range(N):
		if issafe(board, row, col) :
			board[row][col] = 1
			if backtracking_nqueen(board, row+1):
				return True
			board[row][col] = 0

	return False

print(backtracking_nqueen())