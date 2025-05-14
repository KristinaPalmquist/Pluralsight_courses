

class Robot: # parent class
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print('My name is', self.name)
    
    def walk(self, x):
        self.position[0] = self.position[0]+x
        print('New position:', self.position)
        
    def eat(self):
        print("I'm hungry")
        
class Robot_Dog(Robot): # child class
    def make_noise(self):
        print('Woof woof!')
           
    def eat(self):
        super().eat() # calls parents eat method as well
        print("I want dog biscuits!") # method overriding
        
my_robot_dog = Robot_Dog('Bob')
my_robot_dog.walk(10)
my_robot_dog.make_noise()
my_robot_dog.eat()