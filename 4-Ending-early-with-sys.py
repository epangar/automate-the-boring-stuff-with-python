#This code imports sys and random, and exists when the number is 0

import random
import sys

while True:
    n = random.randint(0,9)
    print n

    if n!= 0:
        print('Let\s keep going...')
        continue
    else:
        print('0! Bye!')
        sys.exit()