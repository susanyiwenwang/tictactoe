import random as r

board = [["   ", "|", "   ", "|", "   "], ["   ", "|", "   ", "|", "   "], ["   ", "|", "   ", "|", "   "]]
sample = [[" a ", "|", " b ", "|", " c "], [" d ", "|", " e ", "|", " f "], [" g ", "|", " h ", "|", " i "]]

player_1 = " X "
player_2 = " O "
ai_player = " O "
choices = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
winner = ""

def display(n):
    print(
        f"{' '.join(n[0])}\n----------------\n"
        f"{' '.join(n[1])}\n----------------\n"
        f"{' '.join(n[2])}"
    )


def find_placement(player_move):
    index_1 = None
    index_2 = None
    edited_move = f" {player_move} "
    for board_list in sample:
        if edited_move in board_list:
            index_1 = sample.index(board_list)
            index_2 = board_list.index(edited_move)
    return index_1, index_2


def place_move(placement, player):
    index_1 = placement[0]
    index_2 = placement[1]
    board[index_1][index_2] = player
    display(board)


def check_winner(player):
    global winner
    if player == board[0][0] == board[0][2] == board[0][4]:
        winner = player
    elif player == board[1][0] == board[1][2] == board[1][4]:
        winner = player
    elif player == board[2][0] == board[2][2] == board[2][4]:
        winner = player
    elif player == board[0][0] == board[1][0] == board[2][0]:
        winner = player
    elif player == board[0][2] == board[1][2] == board[2][2]:
        winner = player
    elif player == board[0][4] == board[1][4] == board[2][4]:
        winner = player
    elif player == board[0][0] == board[1][2] == board[2][4]:
        winner = player
    elif player == board[2][0] == board[1][2] == board[0][4]:
        winner = player
    return winner


def determine_winner():
    if not choices and winner == "":
        print("It's a draw!")
    else:
        print(f"Game over. {winner} has won!")


print("Welcome to Tic Tac Toe!")
mode = input("Type '2' for 2-player game, type '1' to play the computer: ")
print("Take a look at the sample board and use the letters to place your 'X' and 'O's.")
display(sample)

while choices:
# player 1's turn
    move = input(f"You are {player_1}. Please choose from the sample above, where you would like to place your mark: ")
    if move in choices:
        place_move(find_placement(move), player_1)
        choices.remove(move)
        if check_winner(player_1) != "":
            break
    else:
        print("Sorry, that choice is not valid. You lose your turn.")

    if not choices:
        break

# player 2's turn
    if mode == 2:
        move = input(f"You are {player_2}. Please choose from the sample above, where you would like to place your mark: ")
        if move in choices:
            place_move(find_placement(move), player_2)
            choices.remove(move)
            if check_winner(player_2) != "":
                break
        else:
            print("Sorry, that choice is not valid. You lose your turn.")

# computer generated 2nd player
    else:
        print("This is the computer's move:")
        ai_move = r.choice(choices)
        place_move(find_placement(ai_move), ai_player)
        choices.remove(ai_move)
        if check_winner(ai_player) != "":
            break

        if not choices:
            break

determine_winner()
