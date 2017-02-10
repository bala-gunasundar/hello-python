#!/usr/bin/python

from random import randrange
import sys

max = 5
guess = randrange(1, 100)
print guess
print "Guessed a number from 1 to 100. Guess it!"

for i in range(0, max):
    print "%s chances left" %(max - i)
    str = raw_input("Enter a number : ")
    if str.lower() == 'q' :
        sys.exit(0)

    ans = int(str)

    if ans == guess:
        print "You got it right !"
        sys.exit(0)

    elif ans > guess:
        print "Greater than the guessed number"

    else:
        print "Smaller than the guessed number"

print 'You lost !'

