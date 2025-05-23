""" USER COMMAND """
while True:
    command = input('Enter command: ')
    match command:
        case 'hi':
            print(f'You just said "{command}"')
        case 'bye':
            print('Leave if you must')
            break
        case _:
            print(f'What do you mean by "{command}"')
            pass
input()

""" DIFFERENT TYPES"""
for x in 1, "two", 3.14159, Exception('oops'), lambda x: x*x:
    match x:
        case int():
            print(f'{x} is an integer')
        case str():
            print(f'{x} is a string')
        case float():
            print(f'{x} is a floating point number')
        case Exception():
            print(f'Something bad happened: {x}')
        case y:
            print(f"Don't know what '{y}' is")
input()

""" GUARDS """        
for i in range(5):
    match i:
        case 1 | 3 | 5 if i < 4:
            print(f'{i} is odd and less than 4')
        case 1 | 3 | 5 if i > 4:
            print(f'{i} is odd and greater than 4')
        case 2 | 4:
            print(f'{i} is even')
input()

""" CAPTURING MATCHED PATTERNS """
for i in 'ABC':
    match i:
        case 'A' as letter_A:
            print(f'"{i}" is "{letter_A}"')
        case str(letter_B) if i == 'B':
            print(f'"{i}" is "{letter_B}"')
        case other_letter:
            print(f'Default case: "{i}" is "{other_letter}"')
input()
            
""" LISTS, TUPLES, AND MAPPING AND WILDCARDS """
for stw in [1,2,3], (4,5,6),(3,4,7), {'a': 42}, (8,5,9):
    match stw:
        case [1,2,3] as my_list:
            print(f'{my_list} is a list')
        case (_,5 as my_int, _) as my_tuple:
            print(f'{my_tuple} is a tuple with item {my_int}')
        case {'a': 42 as the_answer}:
            print(f'The answer is {the_answer}')
input()
            

""" WALRUS MATCHING """
match the_answer := (2 * 3* 7):
    case _:
        print(f'The answer is {the_answer}')
input()