
""" SLOTS """
# provide instances with faster attribute access
# reduces memory overhead
# attributes cannot be added dynamically anymore = static
        
# class Developer:
#     __slots__ = "name", "age", "salary", "framework"
#     def __init__(self, name, age, salary, framework):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.framework = framework
        
# employee2 = Developer(name='Ji-Soo', age=38, salary=1000, framework="Flask") 

# print(employee2.__slots__)



    
class Employee:
    __slots__ = "name", "age", "salary"
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

class Tester(Employee):
    def run_tests(self):
        print(f'Testing is started by {self.name}...')
        print('Tests are done')

class Developer(Employee):
    __slots__ = "framework"
    def __init__(self, name, age, salary, framework):
        self.framework = framework
        super().__init__(name, age, salary)
    def increase_salary(self, percent, bonus=0): 
        super().increase_salary(percent)
        self.salary += bonus
        

employee1 = Tester(name='Lauren', age=44, salary=1000)
employee2 = Developer(name='Ji-Soo', age=38, salary=1000, framework="Flask") 
print(employee2.__slots__)