
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
        return f'{self.name} is {self.age} years old. Employee is a {self.position} with a salary of ${self.salary}'
    def increase_salary(self, percent):
        self.salary += (self.salary * (percent)/100)
        
class Developer(Employee):
    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
    def increase_salary(self, percentage, bonus):
        return super().increase_salary(percentage)
        
class Tester(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
    def run_tests():
        pass

employee1 = Tester(name='Ji-Soo', age=38, salary=1200) 
employee2 = Employee(name='Lauren', age=44, salary=1000)
employee1.salary = 2000
print(employee1.salary)