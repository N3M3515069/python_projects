import random
def guess_game(x):
    
    high = x
    low = 1
    guess = random.randint(1 , x)
    
    feedback = input(f'is {guess} too High(H) or too Low(L) or Correct(C)? '.lower())

    while feedback != 'c' and high != low :
        if feedback == 'h':
            high = guess-1
            guess = random.randint(low,high)
        elif feedback == 'l':
            low = guess+1
            guess = random.randint(low,high)
        feedback = input(f'is {guess} too High(H) or too Low(L) or Correct(C)? '.lower())


    if feedback == 'c' or high == low :
        print(f'yay! the correct number {guess} has been found')

guess_game(10)
