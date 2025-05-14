import os


folder = '/Users/Kristina/Desktop/'
# create folder CleanedUp/ on desktop
# os.mkdir(folder + 'CleanedUp')

# list files in Desktop/ folder
entries = os.scandir(folder)
for entry in entries:
    if os.path.isfile(entry):
        print('File: ', entry.name)
    elif os.path.isdir(entry):
        print('Directory: ', entry.name)
    
# for each file in the Desktop/ folder
    # move the file to the CleanedUp/ folder
    
