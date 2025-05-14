# print('Hello World!')

# greeting = 'Hello'
# name = input("What's your name? \n")
# print(greeting + ' ' + name.capitalize() + '!')

import random

def greeting(name = None, phrase = 'Hello'):
    if name == None:
        print(f'{phrase}!')
    else:
        print(f'{phrase} {name}!')

persons = ['Kiki', 'Anna', 'Bob', 'Sarah', 'Hector']
phrases = ['Tjena', 'Hej', 'Hallå', 'Hello', 'Hi', 'Bonjour', 'Salve', 'Ciao']

for person in persons:
    salutation = random.choice(phrases)
    greeting(person, salutation)
    greeting(person)
    greeting()
    print('')