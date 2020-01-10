'''
Write a function named collatz() that has one parameter named number. If
number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1.
Then write a program that lets the user type in an integer and that keeps
calling collatz() on that number until the function returns the value 1.
'''


def collatz(number):
          
    if number % 2 == 0:
        number = (number / 2)
        
    else:
        number = (number * 3) + 1
        
    return int(number)

try:
    user_input = int( input ('Please input a number: '))
except ValueError:
    print('You must enter an integer type.')
    

print(user_input)

while user_input != 1:
    user_input = collatz(int(user_input))
    print(user_input)