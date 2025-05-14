import random

# roll = random.randint(1,6)

# guess = int(input(f'Guess the dice roll:\n'))

# if roll == guess:
#     print('You win!')

# print(f'The computer rolled a... {int(roll)}')


player1 = input("Enter player 1's name:\n")
player2 = input("Enter player 2's name:\n")



def roll_dice():
    dice_total = random.randint(1,6)+random.randint(1,6)
    return dice_total

def main():
    player1_roll = roll_dice()
    player2_roll = roll_dice()

    print(player1, 'rolled', player1_roll)
    print(player2, 'rolled', player2_roll)

    if player1_roll == player2_roll:
        print('you TIED')
    elif player2_roll > player1_roll:
        print(player2, 'won!')
    else:
        print(player1, 'won. HA ha!')
        
main()