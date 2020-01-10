import Hangman_Words, sys, random

total_tries = 3

def choose_word():
    list = Hangman_Words.words
    le = len(list)-1
    position = random.randint(0, le)
    return list[position]

secret_word = choose_word()
user_total_input_so_far = "-" * len(secret_word)

def ask():
    user_input = input('Please add a character: ')

def check():


def win():
    print ('You won! Congratulations! :D')
    sys.exit()

def lose():
    print ('You lose! Sorry :(')
    sys.exit()

print ('I have chosen a random word. You have 10 tries.')

while total_tries >= 1:

    ask()

    if (total_tries > 1):
        print ('You still have %d tries.' % total_tries)
    elif (total_tries == 1):
        print ('You still have 1 try.')
    
    print (total_tries)
    total_tries -= 1