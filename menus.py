# breakfast = ['Egg sandwich', 'Bagel', 'Coffee']
# lunch = ['BLT', 'PB&J', 'Turkey Sandwich']
# dinner = ['Soup', 'Salad', 'Spaghetti', 'Taco']
# menus = []
# menus.append(breakfast)
# menus.append(lunch)
# menus.append(dinner)
# print('Breakfast Menu:\t', menus[0])
# print('Lunch Menu:\t', menus[1])
# print('Dinner Menu:\t', menus[2])

# print(menus[0][1])


menus = {
    "Breakfast": ['Egg sandwich', 'Bagel', 'Coffee'],
    "Lunch": ['BLT', 'PB&J', 'Turkey Sandwich'],
    "Dinner": ['Soup', 'Salad', 'Spaghetti', 'Taco'],
}

# print('Breakfast Menu:', end=' ')
# for item in menus['Breakfast']:
#     print(item, end=' ')
# print('\nLunch Menu:', end=' ')
# for item in menus['Lunch']:
#     print(item, end=' ')
# print('\nDinner Menu:', end=' ')
# for item in menus['Dinner']:
#     print(item, end=' ')
# print('')

for name, menu in menus.items():
    print(name, ':', sep = '', end=' ')
    for item in menu:
        print(item, end=' ')
    print('')