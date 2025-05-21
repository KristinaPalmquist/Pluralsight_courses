
""" Implementing Class Inheritance"""

# DRY - Don't Repeat Yourself
class Person: # base class / parent class / superclass
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def project_update(self):
        pass
    
class Client(Person): # derived class / child class / subclass
    def __init__(self, name, age):
        super().__init__(name, age)

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    def __str__(self):
        return f'{self.name} is {self.age} years old. Employee has a salary of ${self.salary}'
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)
        
class Developer(Employee):
    def __init__(self, name, age, salary, framework):
        self.framework = framework
        super().__init__(name, age, salary)
    def increase_salary(self, percent, bonus=0): # method overriding
        # self.salary += self.salary * (percent/100)
        super().increase_salary(percent) # dynamic
        # Employee.increase_salary(self, percent) # method resolution order, will have to be changed if hierarchy changes
        self.salary += bonus
        # return super().increase_salary(percent)
        
class Tester(Employee):
    def run_tests(self):
        print(f'Testing is started by {self.name}...')
        print('Tests are done')

employee1 = Tester(name='Lauren', age=44, salary=1000)
employee2 = Developer(name='Ji-Soo', age=38, salary=1000, framework="Flask") 
print(employee2.name)
print(employee2.framework)

# class Employee(object):
#     pass
# e = Employee()
# print(repr(e))

# print(isinstance(employee1, Tester))
# print(isinstance(employee1, Employee))
# print(issubclass(Developer, Employee))
# print(issubclass(Employee, object))
# print(issubclass(Developer, object))

# try:
#     x = 0/7
#     y = 7/0
#     raise ZeroDivisionError('Ojoj')
# except ArithmeticError as e:
#     print('Error!!!', e)
