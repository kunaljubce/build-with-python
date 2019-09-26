import os
from operator import itemgetter

def player_choices(player1_name, player2_name):
    '''Function to assign the player choices i.e. who plays with X and who plays with O'''
    
    choices = {'player1':'', 'player2':''}
    while not(choices['player1'] in ['X', 'O']):
        choices['player1'] = (input("Hi {p1}, enter your choice (X/O): ".format(p1 = player1_name))).upper()
    choices['player2'] = 'O' if choices['player1'] == 'X' else 'X'
    print("Great, let's begin playing! {pn1} will play with {c1}, {pn2} will play with {c2}!" \
                              .format(pn1 = player1_name, pn2 = player2_name, c1 = choices['player1'], c2 = choices['player2']))
    return choices

def game_design(game_pattern):
    '''Function to print Tic Tac Toe board with numbers initially and updated with  X & O as the game continues'''
    
    #clear_output()
    os.system('cls')
    print('\n')
    print(game_pattern[7] + ' | ' + game_pattern[8] + ' | ' + game_pattern[9])
    print('----------')
    print(game_pattern[4] + ' | ' + game_pattern[5] + ' | ' + game_pattern[6])
    print('----------')
    print(game_pattern[1] + ' | ' + game_pattern[2] + ' | ' + game_pattern[3])
    print('\n')

def move_valid(game_pattern, move_id):
    '''Function to check if move entered is valid or not. Also move should not be in a box already marked O or X!'''
    
    if move_id not in range(1, 10) or game_pattern[move_id] in ['X', 'O']:
        print("Invalid move! Choose from the numbers available within the Tic Tac Toe board!")
        return False
    else:
        return True

def game_decider(game_pattern):
    '''Function to check if game has been won or not'''
    
    if len(set(game_pattern[1:4])) == 1 or len(set(game_pattern[4:7])) == 1 or len(set(game_pattern[7:])) == 1 \
        or len(set(itemgetter(1, 4, 7)(game_pattern))) == 1 or len(set(itemgetter(1, 5, 9)(game_pattern))) == 1 \
        or len(set(itemgetter(2, 5, 8)(game_pattern))) == 1 or len(set(itemgetter(3, 6, 9)(game_pattern))) == 1 \
        or len(set(itemgetter(3, 5, 7)(game_pattern))) == 1 :
        return True
    else:
        return False