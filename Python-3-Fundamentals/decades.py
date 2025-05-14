"""
Task 1:
Ask the user for their age and tell them number of decades and years.
"""
# age = int(input('How old are you?\n'))

# years = age % 10

# decades = int((age - years)/10)

# print(f'You are {decades} decades\nand {years} year(s) old')



age = int(input('How old are you?\n'))
decades = age//10
years = age % 10

print("You are " + str(decades) + 
      " decades and " + str(years) + " years old")