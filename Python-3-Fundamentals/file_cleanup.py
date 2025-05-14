import os


# # folder_destination = '/Users/Kristina/Desktop/'
# # new_destination = os.path.join(folder_destination, 'CleanedUp/')
# # print(new_destination)
# # create folder CleanedUp/ on desktop
# # os.mkdir(folder + 'CleanedUp')

# # list files in Desktop/ folder
# # entries = os.scandir(folder_destination)
# # entries = os.scandir(new_destination)
# # for entry in entries:
# #     if os.path.isfile(entry):
# #         print('File: ', entry.name)
# #     elif os.path.isdir(entry):
# #         print('Directory: ', entry.name)
        
# folder_original = '/Users/Kristina/Desktop/'
# # # os.mkdir(folder_original + 'CleanedUp/' + 'Screenshots')
# folder_destination = '/Users/Kristina/Desktop/CleanedUp/Screenshots/'


# location_original = os.path.join(folder_original, 'Screenshot 2025-04-19 at 18.07.15.png')
# location_destination = os.path.join(folder_destination, 'Screenshot 2025-04-19 at 18.07.15.png')
# os.rename(location_original, location_destination)
# # for each file in the Desktop/ folder
#     # move the file to the CleanedUp/ folder
    
""" clean up screenshots """
folder_original = '/Users/Kristina/Desktop/'
folder_destination = '/Users/Kristina/Desktop/CleanedUp/Screenshots/'
for entry in os.scandir(folder_original):
    if os.path.isfile(entry) and entry.name.startswith('Screenshot'):
        location_original = os.path.join(folder_original, entry.name)
        print('File: ', entry.name)
        location_destination = os.path.join(folder_destination, entry.name)
        os.rename(location_original, location_destination)
