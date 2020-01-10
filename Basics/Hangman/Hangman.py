import Hangman_Words, sys, random



def choose_word():
    list = Hangman_Words.words
    le = len(list)-1
    position = random.randint(0, le)
    return list[position]

total_tries = 10
secret_word = choose_word()
guessed_so_far = "-" * len(secret_word)

def update_guessed_so_far(input):
    global guessed_so_far
    guessed_so_far = list(guessed_so_far)

    for j in range(0, len(secret_word)):
        # print (j, secret_word, secret_word[j], guessed_so_far, input)

        if secret_word[j] == input:
            guessed_so_far[j] = input

    guessed_so_far = ''.join(guessed_so_far)



def check(input):
    
    current_input = input.upper()
    if current_input in secret_word:
        print ("Yes, %s appears in the word! Keep going." % current_input)
        update_guessed_so_far(current_input)
    else:
        print ("Nope!")
        global total_tries 
        total_tries -= 1
        
        if (total_tries > 1):
            print ('You still have %d tries.' % total_tries)
        elif (total_tries == 1):
            print ('You still have 1 try.')
    
    global guessed_so_far
    print (guessed_so_far)

def ask():
    
    user_input = input('Please add a character: ')
    check(user_input)


def win():
    print ('You won! Congratulations! :D')
    sys.exit()


def lose():
    print ('You lose! Sorry :(')
    sys.exit()


print ('I have chosen a random word. You have 10 tries.')

while total_tries >= 1:

    ask()

    