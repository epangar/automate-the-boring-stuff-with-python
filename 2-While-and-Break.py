password = 'password'

while True:
    
    user_input = str(raw_input( 'What\'s the password? ' ))

    if user_input != password:
        print('No, that\'s not correct')
        continue
    else:
        print('That\'s correct!')
        break

