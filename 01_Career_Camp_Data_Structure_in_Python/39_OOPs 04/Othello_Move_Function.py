class OthelloBoard:
    player1Symbol = 1
    player2Symbol = 2

    def __init__(self):
        self.board = [[0] * 8 for _ in range(8)]
        self.board[3][3] = self.player1Symbol
        self.board[3][4] = self.player2Symbol
        self.board[4][3] = self.player2Symbol
        self.board[4][4] = self.player1Symbol

    def print_board(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j], end=' ')
            print()

    xDir = [-1, -1, 0, 1, 1, 1, 0, -1]
    yDir = [0, 1, 1, 1, 0, -1, -1, -1]

    def move(self, symbol, x, y):
        if x < 0 or x >= 8 or y < 0 or y >= 8 or self.board[x][y] != 0:
            return False

        move_possible = False
        for i in range(len(self.xDir)):
            xStep = self.xDir[i]
            yStep = self.yDir[i]
            currentX = x + xStep
            currentY = y + yStep
            count = 0

            while 0 <= currentX < 8 and 0 <= currentY < 8:
                if self.board[currentX][currentY] == 0:
                    break
                elif self.board[currentX][currentY] != symbol:
                    currentX += xStep
                    currentY += yStep
                    count += 1
                else:
                    if count > 0:
                        move_possible = True
                        convertX = currentX - xStep
                        convertY = currentY - yStep
                        while convertX != x or convertY != y:
                            self.board[convertX][convertY] = symbol
                            convertX -= xStep
                            convertY -= yStep
                    break
        if move_possible:
            self.board[x][y] = symbol

        return move_possible



def main():
    n = int(input())
    p1Turn = True
    
    player1Symbol = 1
    player2Symbol = 2
    board = OthelloBoard()
    while n > 0:
        x, y = map(int, input().split())
        ans = False
        if p1Turn:
            ans = board.move(player1Symbol, x, y)
        else:
            ans = board.move(player2Symbol, x, y)
        if ans:
            board.print_board()
            p1Turn = not p1Turn
            n -= 1
        else:
            print('false')

if __name__ == '__main__':
    main()