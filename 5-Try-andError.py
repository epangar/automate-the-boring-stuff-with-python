import random

def divide(divisor):
    try:
        return 100 / divisor
    except ZeroDivisionError:
        print('ERROR, DIVIDE BY ZERO')


for i in range (0,20):
    number = random.randint(0,5)
    print number

    print divide(number)