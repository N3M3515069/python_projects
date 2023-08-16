from random import randint
rps_list = ['rock' , 'paper' , 'scissors']

def rps(x):
    pc_points = 0
    user_points = 0
    print(f'THIS IS A {x} ROUND GAME ONE WHO SCORES THE HIGHEST POINTS WINS')
    
    for i in range(x):
        index = randint(0,2)
        user = input('select your weapon rock or paper or scissors: ')
        print(f'user has chosen {user}')
        pc = (rps_list[index])
        print(f'PC has chosen {pc}')
        
        if user == pc:
            print('its a tie')
        elif user == 'rock' and pc == 'scissors':
            print('user won +1')
            user_points += 1
        elif user == 'paper' and pc == 'rock':
            print('user won +1')
            user_points += 1
        elif user == 'scissors' and pc == 'paper':
            print('user won +1')
            user_points += 1
        else:
            print('pc won +1')
            pc_points += 1
    
    if pc_points == user_points:
        print('MATCH DRAW')
    elif pc_points > user_points:
        print(f'PC WON WITH {pc_points} POINTS')
    else:
        print(f'USER WON WITH {user_points} POINTS')

rps(5)

