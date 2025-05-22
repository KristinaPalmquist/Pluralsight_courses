from immutable import Immutable

class Customer(Immutable):
    __slots__ = ('name', 'address', 'enterprise')
    
    def __init__(self, name, address, enterprise):
        super().__init__()
        self.name = name
        self.address = address
        self.enterprise = enterprise
        
    @staticmethod
    def notify(cust, msg):
        print(f'Sending {msg} to {cust.name} at {cust.address}')