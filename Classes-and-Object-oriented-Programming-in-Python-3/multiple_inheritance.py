
""" inherit functionality for more than one parent class
mostly used for Mixin classes

instead of repeating for each class, you can create a mixin class for the functionality that should be shared """
    
class Employee:
    __slots__ = ("name", "age", "salary")
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)
    def has_slots(self):
        print('Inside employee')
        return hasattr(self, "__slots__")    # returns true if second is accessible from first

class SlotsInspectorMixin:
    __slots__ = ()
    # pass
    def has_slots(self):
        return hasattr(self, "__slots__")    # returns true if second is accessible from first

class Developer(SlotsInspectorMixin, Employee):
    __slots__ = ("framework",)
    def __init__(self, name, age, salary, framework):
        self.framework = framework
        super().__init__(name, age, salary)
    def increase_salary(self, percent, bonus=0): 
        super().increase_salary(percent)
        self.salary += bonus

    

employee2 = Developer(name='Ji-Soo', age=38, salary=1000, framework="Flask") 
print(employee2.__slots__)
print(employee2.has_slots())
print(Developer.mro())
print(employee2.__dict__)