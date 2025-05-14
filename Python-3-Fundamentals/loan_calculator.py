

money_owed = float(input('How much money do you owe, in dollars?\n'))
apr = float(input('What is the annual percentage rate of the loan?\n'))
payment = float(input('How much will you pay off each month in dollars?\n'))
months = int(input('How many months do you want to see the result for?\n'))

monthly_rate = apr/100/12

for i in range(months):
    # interest to pay
    interest_paid = money_owed*monthly_rate
    # add interest
    money_owed = money_owed+interest_paid
    if(money_owed - payment < 0):
        print('The last payment is', money_owed)
        print('You paid off the loan in', i+1, 'months')
        break
        
    # make payment
    money_owed -= payment
    print('Paid', payment, 'of which', interest_paid, 'was interest.', end=' ')
    print('Now I owe', money_owed)