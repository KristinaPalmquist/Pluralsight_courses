# import datetime

# dt = datetime.date(1980, 2, 5)
# print(str(dt))
# print(repr(dt))
# print(dt.month)

""" Instantiating Custom Classes """

class Employee:
    # instance methods, work with instances of the class
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
    def __str__(self):
        return f'{self.name} is {self.age} years old. Employee is a {self.position} with a salary of ${self.salary}'
    def increase_salary(self, percentage):
        self.salary += int(self.salary * (percentage)/100)
    def __repr__(self): # representation, more formal, official, should be possible to reproduce instance from the info
        return (f"Employee("
            f"{repr(self.name)}, {repr(self.age)}, "
            f"{repr(self.position)}, {repr(self.salary)})"
        )
        

employee1 = Employee(name='Ji-Soo', age=38, position='developer', salary=1200) # instantiation with instance attributes
employee2 = Employee(name='Lauren', age=44, position='tester', salary=1000)

# print(employee1.__dict__)
# print(employee1.name)
# print(employee1.__class__)
# # Employee.increase_salary(employee2, 20)
# employee2.increase_salary(20)
# print(employee2)
print(repr(employee2))
employee3 = eval(repr(employee2))
print(employee3)