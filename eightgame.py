import random as rd
import copy


def display_board(board):
    for row in board:
        print(f"{row}", end="\n")
    print("-------------------")


def create_board(board_elements):
    #  randomize_board(board_elements)
    #  board = [board_elements[i:i+3] for i in range(0, len(board_elements), 3)]
    #  return board
     return [[0, 1, 3], [4, 2, 5], [7, 8, 6]]


def randomize_board(board_elements):
    rd.shuffle(board_elements)


def final_state():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def game_over(board):
    return board == final_state()


def empty_position(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return (i, j)


def possible_moves(board):
    possibilities = []
    first_flag = 0
    empty = empty_position(board)
    possibilities.append((empty[0]-1, empty[1]))
    possibilities.append((empty[0],   empty[1]+1))
    possibilities.append((empty[0]+1, empty[1]))
    possibilities.append((empty[0],   empty[1]-1))
    if empty[0] == 0:
        first_flag = 1
        possibilities.pop(0)  # this works
    if empty[0] == 2:
        possibilities.pop(-2)  # this works too
    if empty[1] == 0:
        possibilities.pop(-1)  # tis fine as well
    if empty[1] == 2:
        if first_flag:
            possibilities.pop(0)
        else:
            possibilities.pop(1)
    return possibilities


def result(board, action):
    if action not in possible_moves(board):
        print("Invalid Action")
        return
    else:
        empty = empty_position(board)
        number = board[action[0]][action[1]]
        newboard = copy.deepcopy(board)
        newboard[action[0]][action[1]] = 0
        newboard[empty[0]][empty[1]] = number
    return newboard


def position_of_number(board, number):
    for i in range(3):
        for j in range(3):
            if board[i][j] == number:
                return (i, j)


def hamming(board):
    distance = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != final_state()[i][j] and board[i][j] != 0:
                distance +=1
    return distance