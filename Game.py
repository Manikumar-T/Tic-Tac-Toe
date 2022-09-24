# list for Board
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
# variable starting player
player = 'X'
# flage variable for run program
game_end = True
# variable for winners
win = None


# function for display Boards
def welcam_banner():
    print("  __ __ __     ______       __           ______       ______       ___ __ __      ______")
    print(" /_//_//_/\   /_____/\     /_/\         /_____/\     /_____/\     /__//_//_/\    /_____/\\")
    print(" \:\\:\\:\ \    \::::_\/_    \:\ \        \:::__\/     \:::_ \ \    \::\| \| \ \   \::::_\/_")
    print("  \:\\:\\:\ \    \:\/___/\    \:\ \        \:\ \  __    \:\ \ \ \    \:.      \ \   \:\/___/\\")
    print("   \:\\:\\:\ \    \::___\/_    \:\ \____    \:\ \/_/\    \:\ \ \ \    \:.\-/\  \ \   \::___\/_")
    print("    \:\\:\\:\ \    \:\____/\    \:\/___/\    \:\_\ \ \    \:\_\ \ \    \. \  \  \ \   \:\____/\\")
    print("     \_______\/   \_____\/     \_____\/     \_____\/     \_____\/     \__\/ \__\/    \_____\/")
    print()
    print('''
  _____   ___    ___     _____     _      ___     _____    ___    ___      ___     _     __  __   ___ 
 |_   _| |_ _|  / __|   |_   _|   /_\    / __|   |_   _|  / _ \  | __|    / __|   /_\   |  \/  | | __|
   | |    | |  | (__      | |    / _ \  | (__      | |   | (_) | | _|    | (_ |  / _ \  | |\/| | | _| 
   |_|   |___|  \___|     |_|   /_/ \_\  \___|     |_|    \___/  |___|    \___| /_/ \_\ |_|  |_| |___|
   \n''')

welcam_banner()
#x winner banner
def x_winner_banner():
    print('''
 __    __        __                                __                                         
/  |  /  |      /  |                              /  |                                        
$$ |  $$ |      $$/   _______        __   __   __ $$/  _______   _______    ______    ______  
$$  \/$$/       /  | /       |      /  | /  | /  |/  |/       \ /       \  /      \  /      \ 
 $$  $$<        $$ |/$$$$$$$/       $$ | $$ | $$ |$$ |$$$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |
  $$$$  \       $$ |$$      \       $$ | $$ | $$ |$$ |$$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
 $$ /$$  |      $$ | $$$$$$  |      $$ \_$$ \_$$ |$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$/ $$ |      
$$ |  $$ |      $$ |/     $$/       $$   $$   $$/ $$ |$$ |  $$ |$$ |  $$ |$$       |$$ |      
$$/   $$/       $$/ $$$$$$$/         $$$$$/$$$$/  $$/ $$/   $$/ $$/   $$/  $$$$$$$/ $$/       ''')
#o winner banner
def o_winner_banner():
    print('''
  ______         __                                __                                         
 /      \       /  |                              /  |                                        
/$$$$$$  |      $$/   _______        __   __   __ $$/  _______   _______    ______    ______  
$$ |  $$ |      /  | /       |      /  | /  | /  |/  |/       \ /       \  /      \  /      \ 
$$ |  $$ |      $$ |/$$$$$$$/       $$ | $$ | $$ |$$ |$$$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |
$$ |  $$ |      $$ |$$      \       $$ | $$ | $$ |$$ |$$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
$$ \__$$ |      $$ | $$$$$$  |      $$ \_$$ \_$$ |$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$/ $$ |      
$$    $$/       $$ |/     $$/       $$   $$   $$/ $$ |$$ |  $$ |$$ |  $$ |$$       |$$ |      
 $$$$$$/        $$/ $$$$$$$/         $$$$$/$$$$/  $$/ $$/   $$/ $$/   $$/  $$$$$$$/ $$/       ''')
def display_board():
    print(' ' * 10, '  BOARD               POSITION')
    print(' ' * 10, ' =======             ==========')
    print()
    print(' ' * 10, board[0], '|', board[1], '|', board[2], '\t\t', 1, '|', 2, '|', 3)
    print(' ' * 8, '----+---+----         ----+---+----  ')
    print(' ' * 10, board[3], '|', board[4], '|', board[5], '\t\t', 4, '|', 5, '|', 6)
    print(' ' * 8, '----+---+----         ----+---+----  ')
    print(' ' * 10, board[6], '|', board[7], '|', board[8], '\t\t', 7, '|', 8, '|', 9)


# call display_board function
display_board()


# function for switch player
def switch_player():
    global player
    if (player == 'X'):
        player = 'O'
    else:
        player = 'X'


# function to game starting
def start_game():
    while game_end:
        print("It's {} turn".format(player))
        index_str = input('Enter position :')
        if (index_str not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
            start_game()
        else:
            index_int = (int(index_str) - 1)
            if (board[index_int] == '-'):
                board[index_int] = player
            else:
                print('{} is alrady exist in this position {}'.format(board[index_int],index_str))
                start_game()
        display_board()
        check_winner()
        Draw()
        switch_player()
    if (win == 'X' or win == 'O'):
        if(win=='X'):
            x_winner_banner()
            exit()
        else:
            o_winner_banner()
            exit()
    else:
        print('Draw')


# function to check row winners
def row_winner():
    global game_end
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
    if (row1 or row2 or row3):
        game_end = False
    if (row1):
        return board[0]
    elif (row2):
        return board[3]
    elif (row3):
        return board[6]
    else:
        return None


# function to check column Winners
def column_winnner():
    global game_end
    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'
    if (column1 or column2 or column3):
        game_end = False
    if (column1):
        return board[0]
    elif (column2):
        return board[1]
    elif (column3):
        return board[2]
    else:
        return None


# function to check diagonal winners
def diagonal_winner():
    global game_end
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'
    if (diagonal1 or diagonal2):
        game_end = False
    if (diagonal1):
        return board[0]
    elif (diagonal2):
        return board[2]
    else:
        return None


# functin to check Draw
def Draw():
    global game_end
    if ('-' not in board):
        game_end = False


# function to check winner
def check_winner():
    global win, game_end
    winner_row = row_winner()
    winner_column = column_winnner()
    winner_diagonal = diagonal_winner()
    if (winner_row):
        win = winner_row
    elif (winner_column):
        win = winner_column
    elif winner_diagonal:
        win = winner_diagonal


# start game function call
start_game()
