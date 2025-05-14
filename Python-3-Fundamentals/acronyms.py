



# file = open('input.txt')
# try:
    # file.read()
# finally:
    # file.close()


# search_term = input('What acronym would you like to look up? ')

# with open('/Users/kristina/Desktop/input.txt') as file:
#     # result = file.read() # returns whole file as string, or specified number of bytes
#     # print(result)
#     # result = file.readline() # returns next line of the file as string
#     # print(result)
#     # result = file.readline() # returns next line of the file as string
#     # print(result)
#     # result = file.readlines() #returns list of strings
#     # for line in result:
#     #     if search_term.lower() in line.lower():
#     #         print(line)
#     for line in file: # shortcut
#         if search_term.lower() in line.lower():
#             print(line)
#             break
        

# search_term = input('What acronym would you like to look up?')
# definition = ''

# print(search_term, '-', definition)


def find_acronym():
    search_term = input('What acronym would you like to look up? ')
    found = False
    try:
        with open('input.txt') as file:
            for line in file: 
                if search_term.lower() in line.lower():
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print('File not found')
        return
        
    if not found:
        print('The acronym could not be found')

def add_acronym():
    acronym = input('What acr do you want to add? ')
    definition = input('What is the def? ')
    with open('input.txt', 'a') as file:
        file.write(acronym + ' - ' + definition + '\n')
        
def main():
    choice = input('Do want to find (F) or add (A) an acronym? ')
    if choice.upper() == 'F':
        find_acronym()
    elif choice.upper() == 'A':
        add_acronym()
    else:
        'Sorry'
        
main()