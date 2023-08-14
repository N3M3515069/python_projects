def madlibs(*arg):
    
    paragraph = f'''A vacation is when you take a trip to some {adjective1} place
    with your {adjective2} family. Usually you go to some place
    that is near a/an {noun1} or up on a/an {noun2}.
    A good vacation place is one where you can ride {plural_noun1}
    or play {game} or go hunting for {plural_noun2} .'''
        
    print(paragraph)

adjective1 = input('enter an adjective: ')
adjective2 = input('enter an adjective: ')
noun1 = input('enter a noun: ')
noun2 = input('enter a noun: ')
plural_noun1 = input('enter a plural noun: ')
game = input('name a game: ')
plural_noun2 = input('enter a plural noun: ')


madlibs(adjective1 , adjective2 , noun1 , noun2 , plural_noun1 , plural_noun2)