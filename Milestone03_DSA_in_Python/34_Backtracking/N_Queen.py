def is_safe(board, row , col, num_of_queens):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, num_of_queens)):
        if board[i][j] == 1:
            return False
    return True


def solve_n_queen(board, row, num_of_queen):
    if row == num_of_queen:
        for i in range(num_of_queen):
            for j in range(num_of_queen):
                print(board[i][j], end=' ')
        print()
        return
    for col in range(num_of_queen):
        if is_safe(board, row, col, num_of_queen):
            board[row][col] = 1
            solve_n_queen(board, row+1, num_of_queen)
            board[row][col] = 0


def nQueen(num_of_queen):
    board = [[0 for _ in range(num_of_queen)] for _ in range(num_of_queen)]
    solve_n_queen(board, 0, num_of_queen)


def main():
    n = int(input())
    nQueen(n)


if __name__ == '__main__':
    main()

        