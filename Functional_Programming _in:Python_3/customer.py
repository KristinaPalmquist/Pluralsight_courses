from dataclasses import dataclass

@dataclass(frozen=True)
class Customer:
    name: str
    address: str
    enterprise: bool
    
    def __init__(self, name, address, enterprise):
        super().__init__()
        self.name = name
        self.address = address
        self.enterprise = enterprise
        
    @staticmethod
    def notify(cust, msg):
        print(f'Sending {msg} to {cust.name} at {cust.address}')