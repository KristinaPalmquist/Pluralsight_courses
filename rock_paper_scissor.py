# computer_choice = 'scissors'
# user_choice = input('Do you want rock, paper or scissors?\n').lower()

# if computer_choice == user_choice:
#     print('TIE')
# elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissor' and computer_choice == 'paper'):
#     print('You WIN!')
# elif user_choice == 'paper' and computer_choice == 'scissors':
#         print('Computer wins and you lost :(')

import random 

computer_choice = random.choice(['rock', 'paper', 'scissors'])

user_choice = input('Do you want rock, paper or scissors?\n').lower()

print('Computer: ' + computer_choice)

if computer_choice == user_choice:
    print('TIE')
elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissor' and computer_choice == 'paper'):
    print('You WIN!')
    print(user_choice.upper() + ' beats ' + computer_choice.upper())
else:
    print('Computer wins and you lost :( because ' + computer_choice.upper() + ' beats ' + user_choice.upper())