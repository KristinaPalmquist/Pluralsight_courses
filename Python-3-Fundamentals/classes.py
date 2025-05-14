
class Robot_Dog:
    def __init__(self, name_val, breed_val):
        self.name = name_val
        self.breed = breed_val
    def bark(self):
        print('Woof woof!')
        
        
my_dog = Robot_Dog('Ragnar', 'Chihuahua')
print(f'My dog is a {my_dog.breed} called {my_dog.name}')
my_dog.bark()