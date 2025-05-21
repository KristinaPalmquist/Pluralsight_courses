""" DATA CLASSES """

# class Project:
#     def __init__(self, name, payment, client):
#         self.name = name
#         self.payment = payment
#         self.client = client
        
#     def __repr__(self):
#         return f"Project(name={repr(self.name)}, payment={repr(self.payment)}, client={repr(self.client)})"
        

# class Employee:
#     def __init__(self, name, age, salary, project):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.project = project
        
        
# p = Project('Husby', 2000, 'Hasse')
# print(p)
# e = Employee('Hans', 45, 1000, p) # composition, has-a relationship
# print(e.project)

from dataclasses import dataclass
# from typing import Any # can be used when specific type cannot be used

# @dataclass
# class Project: # will cerate __init__ and __repr__ in the background automatically
#      name: str # type hints
#      payment: int
#      client: str
     
#      def notify_client(self):
#          print(f'Notifying the client about the grogress of the {self.name}...')
       

# class Employee:
#     def __init__(self, name, age, salary, project):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.project = project
        
        
# p = Project('Husby', 2000, 'Hasse')
# print(p)
# e = Employee('Hans', 45, 1000, p)
# print(e.project)



@dataclass(slots=True) 
class Project:
     name: str 
     payment: int
     client: str
     
     def notify_client(self):
         print(f'Notifying the client about the grogress of the {self.name}...')
       

class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project
        
        
p = Project('Husby', 2000, 'Hasse')
print(p)
e = Employee('Hans', 45, 1000, p)
print(e.project)