import itertools

def check_same(list):
    if list.count(list[0]) == len(list) and list[0] != 0:
        return True
    else:
        return False


def win_horizontal(current_game):
    for row in current_game:
        if check_same(row):
           print(f"Player {row[0]} is the Winner!!! won horizontally (---) !")
           return True
    return False
def win_vertical(current_game):
    for col in range(len(current_game)):
        indeces = []

        for row in current_game:
            indeces.append(row[col])

        if check_same(indeces):
             print(f"Player {indeces[0]} is the Winner!!! won vertically (|) !")
             return True

    return False

def win_diagonal(current_game):
    diagz_back = []
    for ix in range(len(current_game)):
        diagz_back.append(current_game[ix][ix])

    if check_same(diagz_back):
        print(f"Player {diagz_back[0]} is the Winner!!! won diagonally (back slash \\ )!")
        return True

    cols = reversed(range(len(current_game)))
    rows = range(len(current_game))

    diagz_forward = []

    for col, row in zip(cols,rows):
        diagz_forward.append(current_game[col][row])

    if check_same(diagz_forward):
        print(f"Player {diagz_forward[0]} is the Winner!!! won diagonally (foward slash / )!")
        return True

    return False

def check_win(current_game):
    if win_diagonal(current_game):
        return True
    elif win_vertical(current_game):
        return True
    elif win_horizontal(current_game):
        return True

def game_board(game_map,player=0,row=0,column=0,just_display=False):
    try:
        if game_map[row][column] != 0:
            print(f"This position {row},{column} is taken! Choose another")
            return game_map, False
        print("   " + "  ".join([str(i) for i in range(len(game_map))]))
        if(not just_display):
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count,row)
        return game_map, True
    except IndexError as e:
        print("row and column should be between 0 and 2 inclusive!")
        return game_map, False
    except Exception as e:
        print("Something went wrong!", e)
        return game_map, False

     
run = True
players = [1,2]

while run:
    game_size = 0
    while(game_size < 3):
        print("Minimum size is 3!")
        game_size = int(input("Tic Tac Toe game size?"))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player is: {current_player}")
        played = False

        while not played:
            try:
                col_choice = int(input("What column do you wanna play? (0 , 1 , 2) "))
                row_choice = int(input("What row do you wanna play? (0 , 1 , 2) "))
                game, played = game_board(game, current_player, row_choice, col_choice)
            except Exception as e:
                print("Not valid value! Try all over again!")
                continue

        if check_win(game):
            print("done")
            game_won = True
            play_again = input("Game is over! Would you like to play again? (y) for yes! Anything else for no! ")
            if play_again.lower() == "y":
                print("Restarting!")
            else:
                print("Adios!")
                run = False
            
