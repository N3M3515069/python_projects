import random

def guesser(x):
    
    random_number = random.randint(1,x)

    guess = int(input(f'guess a number between 1 and {x}: '))

    while guess != random_number:
        
        if guess > random_number:
            print('sorry, guess again, too high')
        else:
            print('sorry, guess again, too low')
        
        guess = int(input(f'guess a number again between 1 and {x}: '))

    if guess == random_number:
        print(f'congratulation {guess} is the correct number')

guesser(10)