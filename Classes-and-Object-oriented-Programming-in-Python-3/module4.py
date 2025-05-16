
""" Managing Attribute Access """

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
    def __str__(self):
        return f'{self.name} is {self.age} years old. Employee is a {self.position} with a salary of ${self.salary}'
    def increase_salary(self, percentage):
        self.set_salary(int(self.salary * (percentage)/100))
    def __repr__(self):
        return (f"Employee("
            f"{repr(self.name)}, {repr(self.age)}, "
            f"{repr(self.position)}, {repr(self.salary)})"
        )
    # def get_salary(self):
    #     # return f'${self.salary}'
    #     # return round(self.salary, 2)
    #     # logging.info('Someone accessed the salary attribute')
    #     return self._salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is $1000')
        self._salary = salary
        

employee1 = Employee(name='Ji-Soo', age=38, position='developer', salary=1200) 
employee2 = Employee(name='Lauren', age=44, position='tester', salary=1000)
employee1.salary = 2000
print(employee1.salary)
# print(employee1._salary)
# print(employee1)









