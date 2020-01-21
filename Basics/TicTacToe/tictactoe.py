import random

board = {
  "UL": " ", "UM": " ", "UR": " ",
  "ML": " ", "MM": " ", "MR": " ",
  "DL": " ", "DM": " ", "DR": " ",
}

def print_board():
    print(board['UL'] + '|' + board['UM'] + '|' + board['UR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['DL'] + '|' + board['DM'] + '|' + board['DR'])




def toss_coin():
    return ['False','True'][random.randint(0,1)]


#while(" " in board.values()):
