import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

board =  [['.' for i in range(15)] for i in range(15)]
board_moves = []
def print_board(board):
    for row in board:
        for element in row:
            print(element, end=' ')
        print()

def make_move(board, player, sign):
    row, col = player.move(board)
    board[row][col] = sign

#todo increase performance, refactor
def win_condition_check(board):

    dim = len(board)

    #check horizontal win condition
    for x in range(dim-4):
        for y in range(dim):

            current_sign = board[x][y]
            if current_sign == '.':
                continue
            is_win = True
            for z in range(0, 5):
                if board[x][y+z] != current_sign:
                    is_win = False
                    break
            if is_win:
                return '-', x, y

    #check vertical win condition
    for x in range(dim):
        for y in range(dim - 4):
            current_sign = board[x][y]
            if current_sign == '.':
                continue
            is_win = True
            for z in range(0, 5):
                if board[x+z][y] != current_sign:
                    is_win = False
                    break
            if is_win:
                return '|', x, y

    #check diagonal win condition
    for x in range(dim-4):
        for y in range(x+1):
            current_sign = board[x][y]
            if current_sign == '.':
                continue
            is_win = True
            for z in range(0, 5):
                if board[x+z][y+z] != current_sign:
                    is_win = False
                    break
            if is_win:
                return '\\', x, y

    #check diagonal win condition
    for x in range(dim-4):
        for y in range(x, dim-4):
            current_sign = board[x][y]
            if current_sign == '.':
                continue
            is_win = True
            for z in range(0, 5):
                if board[x+z][y+z] != current_sign:
                    is_win = False
                    break
            if is_win:
                return '\'1', x, y
    return False

class Player:

    def __init__(self, player_name):
        self.player_name = player_name

    def move(self, board):
        row, col = map(int, input().split())
        board_moves.append((row, col))
        return row-1, col-1


if __name__ == '__main__':
    print_board(board)

    while True:
        player_1 = Player('P1')
        player_2 = Player('P2')
        make_move(board, player_1, 'x')
        clearConsole()
        print_board(board)
        if win_condition_check(board):
            break
        make_move(board, player_2, 'o')
        clearConsole()
        print_board(board)
        if win_condition_check(board):
            break
    print(win_condition_check(board))