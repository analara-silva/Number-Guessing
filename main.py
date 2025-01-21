from time import sleep

def level(dif):
    level = ['Easy', 'Medium', 'Hard']
    chances = {
        'Easy': 10, 'Medium': 5, 'Hard': 3
    }
    difficult = level[dif - 1]
    option = chances[difficult]
    print(f'Great! You have selected the {difficult} difficulty level.')
    return option

def game(opt = 5):
    from random import randint
    
    number = randint(1, 100)
    print(number)
    
    bets = 0
    
    while True:
        
        if opt > 0:
            play = int(input('\nEnter your guess: '))
            
            if play != number:
                opt -= 1
                bets += 1
                print('Incorrect!', end=' ')
                
                if play > number:
                    print(f'The number is less than {play}.')
                    
                else:
                    print(f'The number is greater than {play}.')
                    
            else:
                bets += 1
                print(f'Congratulations! You guessed the correct number in {bets} attempts.')
                break
            
        elif opt == 0:
            print('\nGame Over! Your chances are over.')
            print(f'the number I thought was {number}.')
            break
            
            
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
print('You have a multiple chances to guess the correct number\n')



print('Please select the difficulty level:')
print('[1] Easy (10 chances)')
print('[2] Medium (5 chances)')
print('[3] Hard (3 chances)\n')


while True:
    difficult = int(input('Enter your choice: '))
    if difficult in [1, 2, 3]:
        print('Great!')
        break   
    else:
        print('\nThis option is incorrect!\n')
        
opt = level(difficult)
print("Let's start the game!")
game(opt)
        
