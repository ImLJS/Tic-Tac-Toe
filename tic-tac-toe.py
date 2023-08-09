import random
import os

board = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
}

def place_marker(board, marker, position):
    if board[position] == ' ':
        board[position] = marker
    else:
        position = input('Please enter a valid position: ')

def space_check(board, position):
    return board[position] == ' '

def computer_move(board):
    print('Computers turn')
    possible_moves = [x for x, y in board.items() if y == ' ']
    random.shuffle(possible_moves)
    move = possible_moves[0]
    return move

def player_move(board):
    print('Players turn')
    position = input('Please enter a position: ')
    return position

def print_board(board):
    print(f'{board["top-L"]} | {board["top-M"]} | {board["top-R"]}')
    print('- + - + -')
    print(f'{board["mid-L"]} | {board["mid-M"]} | {board["mid-R"]}')
    print('- + - + -')
    print(f'{board["low-L"]} | {board["low-M"]} | {board["low-R"]}')

def check_win(board):
    # refactor code to prevent empty board from winning
    if board['top-L'] == board['top-M'] == board['top-R'] != ' ' or \
        board['mid-L'] == board['mid-M'] == board['mid-R'] != ' ' or \
        board['low-L'] == board['low-M'] == board['low-R'] != ' ' or \
        board['top-L'] == board['mid-L'] == board['low-L'] != ' ' or \
        board['top-M'] == board['mid-M'] == board['low-M'] != ' ' or \
        board['top-R'] == board['mid-R'] == board['low-R'] != ' ' or \
        board['top-L'] == board['mid-M'] == board['low-R'] != ' ' or \
        board['top-R'] == board['mid-L'] == board['low-M'] != ' ':


        return True
    
    # check for tie
    if ' ' not in board.values():

        return True


def turn(XorO):
    if XorO == 'X':
        return 'O'
    else:
        return 'X'

if __name__ == '__main__':
    print('Welcome to Tic Tac Toe!')
    playagain = 'Y'

    while playagain == 'Y':

        print('Do you want to be X or O?')
        XorO = input().upper()
        player_turn = XorO
        computer_turn = turn(XorO)

        while not check_win(board):

            position = player_move(board)
            place_marker(board, player_turn, position)
            print_board(board)
            if check_win(board):
                print(f'{player_turn} wins!')
                break

            position = computer_move(board)
            place_marker(board, computer_turn, position)
            print_board(board)
            if check_win(board):
                print(f'{computer_turn} wins!')
                break

        playagain = input('Do you want to play again? ')
        os.system('cls')