def isSafe(board, row, col): 
    return all(board[i] != col and abs(board[i] - col) != abs(i - row) for i in range(row))
def solve(board, row):
    if row == len(board): return True
    for col in range(len(board)):
        if isSafe(board, row, col):
            board[row] = col
            if solve(board, row + 1): return True
            board[row] = -1
    return False
def solve8Queens():
    board = [-1] * 8
    if solve(board, 0): print('\n'.join(' '.join('Q' if i == row else '.' for i in range(8)) for row in board))
    else: print("No solution.")
solve8Queens()
