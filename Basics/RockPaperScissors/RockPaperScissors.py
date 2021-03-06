import sys, random

score = {
        "computer": 0,
        "player": 0
    }
choices = ['Rock', 'Paper', 'Scissors']

def ask_how_many_turns():
    turns = int(input('How many turns do you want to play?\n>>> '))
    return turns

def computer_choice():
    print("The computer has made its choice.")
    return choices[random.randint(0,2)]

def my_choice():
    choice = int(input('Whats your choice?\n 0) Rock\n 1) Paper\n 2) Scissors\n>>> '))

    if choice not in range(0,2):
        print('I\'m sorry, I don\'t understand')
    
    elif  choice < 0 or choice > 2:
        print('I\'m sorry, I don\'t understand.\n')
        my_choice()
    else:
        
        return choices[choice]

def decide(computer, player):
    print("The computer chose %s, you chose %s." % (computer, player))

    if computer == player:
        print("It\'s a tie!")
        return "tie"
    elif (computer == "Rock" and player == "Scissors") or (computer == "Paper" and player == "Rock") or (computer == "Scissors" and player == "Paper"):
        print("The computer wins this round!")
        return "computer"
    else:
        print("You win this round!")
        return "player"


def play_round(n):
    print("Round number #%r" % n)
    
    adversary_choice = computer_choice()
    player_choice = my_choice()

    winner = decide(adversary_choice, player_choice)
    return winner

def end_game(score):
    if score['player'] == score['computer']:
        print( 'It\'s a tie! Better luck next time.')
    elif score['player'] > score['computer']:
        print('You won! Congratulations!')
    else:
        print('The computer won! Better luck next time.') 
    sys.exit()

def game():

    rounds = ask_how_many_turns()
    print ('We\'ll play %d rounds, then' % rounds)

    for i in range (0, rounds):
        key = str(play_round(i+1))
        if key == "tie":
            pass
        else:
            score[key] += 1
        print ('[ %r - %r ]\n' % (score['computer'], score['player']))
    end_game(score)

game()