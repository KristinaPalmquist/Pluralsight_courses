from dataclasses import dataclass


@dataclass(frozen=True)
class OrderItem:
    name: str
    itemnumber: int
    quantity: int
    price: float
    backordered: bool
    
    def __init__(self, name, itemnumber, quantity, price, backordered):
        super().__init__()
        self.name = name
        self.itemnumber = itemnumber
        self.quantity = quantity
        self.price = price
        self.backordered = backordered
        
    