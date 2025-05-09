import random

roll = random.randint(1,6)

guess = int(input(f'Guess the dice roll:\n'))

if roll == guess:
    print('You win!')

print(f'The computer rolled a... {int(roll)}')