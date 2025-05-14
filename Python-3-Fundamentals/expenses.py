
# expenses = [10.5, 8 , 5, 15, 20, 5, 3]

# sum = 0

# for price in expenses:
#     sum += price
#     print(f'After adding ${price}, sum is now ${sum}.')
# print(f'All your lunches add up to ${sum}')
# print('You spent $', sum, sep='')
    
# tot = sum(expenses)
    
# print(f'All your lunches add up to ${tot}')
# print('You spent $', tot, sep='')


num_expenses = input('How many expenses do you want to register?\n')
expenses = []

for i in range(int(num_expenses)):
    expenses.append(float(input("Enter an expense:\n")))
    
print(expenses)