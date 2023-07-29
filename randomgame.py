import sys
import random
start = sys.argv[1]
end = sys.argv[2]

num = random.randint(int(start), int(end))


def guess(arg):
    while arg != num:
        arg = int(input('enter a number again: '))
    if arg == num:
        return 'Correct! das ist your size bruder!'


print(guess(int(input(f'Guess a number between {start} and {end}: '))))
