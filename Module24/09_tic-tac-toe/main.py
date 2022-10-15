class Cell:
    def __init__(self, num):
        self.num = num
        self.value = " "


class Board:
    def __init__(self):
        self.board = [Cell(i_cell) for i_cell in range(1, 10)]

    def check(self, cell):
        if cell.value == " ":
            return True
        else:
            return False

    def printBoard(self):
        count_cells = 0
        for col in range(3):
            if col != 0:
                print("-" * 9)
            for row in range(3):
                for index, cell in enumerate(self.board):
                    if count_cells == index:
                        if row != 2:
                            print(cell.value, "| ", end="")
                        else:
                            print(cell.value, end="")
                        count_cells += 1
                        break
            print()

    def isWin(self):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if self.board[each[0]].value == self.board[each[1]].value == self.board[each[2]].value:
                if self.board[each[0]].value in ("X", "0"):
                    return self.board[each[0]].value
        return False


class Player:
    def __init__(self, name, figure, board):
        self.name = name
        self.figure = figure
        self.board = board

    def playerMove(self, num_cell):
        for cell in board1.board:
            if cell.num == num_cell and self.board.check(cell):
                cell.num = num_cell
                cell.value = self.figure
                break


board1 = Board()
player1 = Player("Ален", "X", board1)
player2 = Player("Хатуна", "O", board1)

counter = 0
win = False

while not win:
    for i_player in [player1, player2]:
        board1.printBoard()
        num_cell = int(input("Игрок {} ваш ход: ".format(i_player.name)))
        i_player.playerMove(num_cell)
        counter += 1
        if counter >= 4:
            tmp = board1.isWin()
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья")
            win = True
            break