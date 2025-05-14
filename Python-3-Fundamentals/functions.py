# import random

# print('Hello')

# name = input('Enter your name:\n')
# amount = int(21.45)
# roll = random.randint(1,6)


# print(amount)
# print(roll)

def addition(a, b):
    return a + b

def main():
    num1 = float(input('Enter first number:\n'))
    num2 = float(input('Enter second number:\n'))
    result = addition(num1, num2)
    print('The result is', result)
    
main()