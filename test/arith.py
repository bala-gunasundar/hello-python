from random import randrange
from hello import hello

operator = ['+', '-', '/', '*']

for i in range(0, 3):
    a = randrange(1, 100)
    b = randrange(1, 100)
    c = randrange(0, 3)

    op = operator[c]

    if c == 0:
        res = a + b
    elif c == 1:
        if a < b:
            a, b = b, a
        res = a - b
    elif c == 2:
        if a < b:
            a, b = b, a

        res = a / b
    elif c == 3:
        res = a * b
    else:
        print 'Invalid operator'
        sys.exit()

    print '%d %c %d = ?' %(a, op, b)
    print res
    input = raw_input("Enter your input: ");
    if int(input) == res:
        print 'Correct !'
    else:
        print 'Wrong'

print 'Game over'
