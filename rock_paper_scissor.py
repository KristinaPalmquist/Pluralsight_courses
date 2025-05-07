computer_choice = 'scissors'
user_choice = input('Do you want rock, paper or scissors?\n')

if computer_choice == user_choice:
    print('TIE')
elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissor' and computer_choice == 'paper'):
    print('You WIN!')
else:
    print('Computer wins and you lost :(')
