from itertools import takewhile
from order import Order








# option 1: for loop
for oi in Order.get_order_details(Order.orders):
    if oi.orderid > 2: break
    print(f'{oi.customer}: {oi.item} at ${oi.total_price}')
    
# option 2: for loop using takewhile
for oi in takewhile(lambda oi: oi.orderid < 1, Order.get_order_details(Order.orders)):
    print(f'{oi.customer}: {oi.item} at ${oi.total_price}')
    
# option 3: print using iterable unpacking
print(*map(lambda oi: f'{oi.customer}: {oi.item} at ${oi.total_price}\n',
           takewhile(lambda oi: oi.orderid < 3, Order.get_order_details(Order.orders))))    
    
    