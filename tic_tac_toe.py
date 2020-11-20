import re
import sys
import random
import os
import time


def init_board():  
    board = [[" ", "1", "2", "3"],
            ["A", ".",".","."],
            ["B", ".",".","."],
            ["C",".",".","."]]
    return board


def init_player():
    player = input ("Insert your name: ")
    if player == "quit":
        print("Thanks for playing")
        sys.exit()
    return player


def get_move(board, player):
    # """Returns the coordinates of a valid move for player on board."""
    move =  input ("Please insert a coordonate: " )
    valid_moves = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    if move == "quit":
        print("Thanks for playing")
        sys.exit()
    while move not in valid_moves:
        move = input ("Invalid move, please chose again: ")
    if move == "quit":
        print("Thanks for playing")
        sys.exit()
    row, col = 0, 0
    if move == "A1":
        row, col = 1, 1
    elif move == "A2":
        row, col = 1, 2
    elif move == "A3":
        row, col = 1, 3
    elif move == "B1":
        row, col = 2, 1
    elif move == "B2":
        row, col = 2, 2
    elif move == "B3":
        row, col = 2, 3
    elif move == "C1":
        row, col = 3, 1
    elif move == "C2":
        row, col = 3, 2
    elif move == "C3":
        row, col = 3, 3
    print(row,col)
    return row, col


def get_ai_move(board, ai_move):
    """Returns the coordinates of a valid move for AI on board."""
   
    valid_moves_ai = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    time.sleep(0.5)
    ai_move = random.choice(valid_moves_ai)
    while ai_move not in valid_moves_ai:
        ai_move = random.choice(valid_moves_ai)
    row, col = 0, 0
    if ai_move == "A1":
        row, col = 1, 1
    elif ai_move == "A2":
        row, col = 1, 2
    elif ai_move == "A3":
        row, col = 1, 3
    elif ai_move == "B1":
        row, col = 2, 1
    elif ai_move == "B2":
        row, col = 2, 2
    elif ai_move == "B3":
        row, col = 2, 3
    elif ai_move == "C1":
        row, col = 3, 1
    elif ai_move == "C2":
        row, col = 3, 2
    elif ai_move == "C3":
        row, col = 3, 3
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    if board[row][col] == ".":
        board[row][col] = player
        return True
    else:
        return False


def has_won(board, player):    
    # """Returns True if player has won the game."""
        if board[1][1] == board[1][2] == board[1][3] == player:
            return True
        elif board[2][1] == board[2][2] == board[2][3] == player:
            return True
        elif board[3][1] == board[3][2] == board[3][3] == player:
            return True
        elif board[1][1] == board[2][1] == board[3][1] == player:
            return True
        elif board[2][1] == board[2][2] == board[3][2] == player:
            return True
        elif board[3][1] == board[3][2] == board[3][3] == player:
            return True
        elif board[1][1] == board[2][2] == board[3][3] == player:
            return True
        elif board[3][1] == board[2][2] == board[1][3] == player:
            return True
        else:
            return False                                       


def is_full(board):
# """Returns True if board is full.""" 
    if "." in board[1]:
        return False
    elif "." in board[2]:
        return False
    elif "." in board[3]:
        return False
    else:
        return True 


def print_board(board):
#     """Prints a 3-by-3 board on the screen with borders."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(board[0][0], "  ", board[0][1], "  ", board[0][2], "   ", board[0][3])
    print(board[1][0],"  ", board[1][1], "" + "| ", board[1][2], " | ", board[1][3])
    print("   ----+-----+-----")
    print(board[2][0],"  ", board[2][1], "" + "| ", board[2][2], " | ", board[2][3])
    print("   ----+-----+-----")
    print(board[3][0],"  ", board[3][1], "" + "| ", board[3][2], " | ", board[3][3])
    print()


def print_result(winner):
#     """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == "X" or winner == "0":
        print(winner + " has won!")
    else:
        print("It's a tie!!")


def tictactoe_game_hh(mode='HUMAN-HUMAN'):
    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    board = init_board()
    print_board(board)
    current_player = "0"
    while not has_won(board,current_player) and not is_full(board):
        if current_player == "0":
            current_player = "X"
        else:
            current_player = "0"
        row, col = get_move(board, current_player)
        while not mark(board, current_player, row, col):
            print("This position is taken!")
            row, col = get_move(board, current_player)
        print_board(board)
    if has_won(board, current_player):
        print_result(current_player)
    else:
        print_result(1)


def tictactoe_game_ha(mode='HUMAN-AI'):
    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    board = init_board()
    print_board(board)
    current_player = "0"     
    while not has_won(board,current_player) and not is_full(board):
        if current_player == "0":
            current_player = "X"
            row, col = get_move(board, current_player)
        else:
            current_player = "0"
            # time.sleep(0.5)
            row, col = get_ai_move(board, current_player)
        while not mark(board, current_player, row, col):
            row, col = get_ai_move(board, current_player)
        print_board(board)
    if has_won(board, current_player):
        print_result(current_player)
    else:
        print_result(1)


def tictactoe_game_ah(mode='AI-HUMAN'):
    board = init_board()
    print_board(board)
    current_player = "0"
    while not has_won(board,current_player) and not is_full(board):
        if current_player == "0":
            current_player = "X"
            row, col = get_ai_move(board, current_player)
        else:
            current_player = "0"
            row, col = get_move(board, current_player)
        while not mark(board, current_player, row, col):
            print("This position is taken!")
            row, col = get_ai_move(board, current_player)
        print_board(board)
    if has_won(board, current_player):
        print_result(current_player)
    else:
        print_result(1)        
  

def tictactoe_game_ai(mode='AI-AI'):
    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    board = init_board()
    print_board(board)
    current_player = "0"     
    while not has_won(board,current_player) and not is_full(board):
        if current_player == "0":
            current_player = "X"
            row, col = get_ai_move(board, current_player)
            print_board(board)
        else:
            current_player = "0"
        row, col = get_ai_move(board, current_player)
        while not mark(board, current_player, row, col):
            # print("This position is taken!")
            row, col = get_ai_move(board, current_player)
            # get_ai_move(board, current_player)
        print_board(board)
    if has_won(board, current_player):
        print_result(current_player)
    else:
        print_result(1)


def game_mode():
    game_mode = input("\n""Please select the game mode \n" 
            "Press '1' to play Human vs. Human \n"
            "Press '2' to play Human vs. AI \n"
            "Press '3' to play AI vs. Human \n"
            "Press '4' to play AI vs. AI: " )
    if game_mode == "quit":
        print("Thanks for playing")
        sys.exit()      
    if game_mode == "1":
        game_mode = tictactoe_game_hh('HUMAN-HUMAN')
    elif game_mode == "2":
        game_mode = tictactoe_game_ha('HUMAN-AI')
    elif game_mode == "3":
        game_mode = tictactoe_game_ah('AI-HUMAN')
    else:
        game_mode == "4"
        game_mode = tictactoe_game_ai('AI-AI')


def main_menu():
    
    player1_name = init_player()   
    print(player1_name, "You will play X!""\n")
    player2_name = init_player()
    print(player2_name, "You will play 0!")
    game_mode()


if __name__ == '__main__':
    main_menu()


