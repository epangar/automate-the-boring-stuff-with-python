import random, sys

print('You have 3 chances to guess the number, between 1 and 10')

current_guesses = 0
secret_number = random.randint(1, 10)

print(secret_number)

while current_guesses < 3:
    user_input = int(input( 'Guess the number: ' ))

    if secret_number == user_input:
        print('That is correct! Bye!')
        sys.exit()
    elif secret_number > user_input:
        print('Bigger!')
        current_guesses += 1
        continue
    elif secret_number < user_input:
        print('Lower!')
        current_guesses += 1
        continue
    

if (current_guesses == 3):
    print('You lose! :(')
    sys.exit()