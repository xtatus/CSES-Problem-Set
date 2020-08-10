
def check_l(x, y, board):
    if board[x][y - 1] == 1:
        return False
    else:
        if board[x][y - 2] == 1 and board[x+1][y-1] == 0 and board[x-1][y-1] == 0:
            return False
        else:
            return True

def check_d(x, y, board):
    if board[x + 1][y] == 1:
        return False
    else:
        if board[x+2][y] == 1 and board[x+1][y+1] == 0 and board[x+1][y-1] == 0:
            return False
        else:
            return True

def check_u(x, y, board):
    if board[x - 1][y] == 1:
        return False
    else:
        if board[x - 2][y] == 1 and board[x-1][y+1] == 0 and board[x-1][y+1]:
            return False
        else:
            return True

def check_r(x, y, board):
    if board[x][y + 1] == 1:
        return False
    else:
        if board[x][y+2] == 1 and board[x+1][y+1] == 0 and board[x-1][y+1] == 0:
            return False
        else:
            return True


def path_finder(move_n, x, y, board, cout, path):


    #print(move_n)
    if (x,y) == (7,1):
        if move_n == 48:
            return cout+1
        else:
            return cout

    for move in ["R", "D", "U", "L"]:
        if path[move_n] == move or path[move_n] == "?":
            if check_moves[move](x, y, board):
                #print(move)
                move_n+=1
                delta_x, delta_y = moves[move]
                board[x + delta_x][y + delta_y] = 1

                cout = path_finder(move_n, x + delta_x, y + delta_y, board, cout, path)

                # back track
                move_n -= 1
                board[x+delta_x][y+delta_y] = 0

    return cout


def main():
    path = input()
    anwser = ""

    board = [[0 for j in range(9)] for i in range(9)]
    board[0] = [1,1,1,1,1,1,1,1,1]
    board[8] = [1,1,1,1,1,1,1,1,1]

    board[1][1] = 1

    for i in range(1,9):
        board[i][0] = 1
        board[i][8] = 1


    # start position
    (x,y) = (1,1)

    print(path_finder(0, x, y, board, 0, path))

    
if __name__ == "__main__":

    check_moves = {
        "D" : check_d,
        "U" : check_u,
        "R" : check_r,
        "L" : check_l
    }

    moves = {
        "L": (0, -1),
        "U": (-1, 0),
        "D": (1, 0),
        "R": (0, 1)
    }

    main()
