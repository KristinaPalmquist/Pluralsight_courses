
# def remainer_division(a, b):
#     try:
#         result = a//b
#         remainder = a%b
#         print(a, '/', b, 'is', result, 'remainder', remainder)
#     except:
#         print('not possible')
        
# def remainer_division(a, b):
#     if b == 0:
#         raise ZeroDivisionError
#     result = a//b
#     remainder = a%b
#     print(a, '/', b, 'is', result, 'remainder', remainder)
#     print('not possible')

        
def remainer_division(a, b):
    if b == 0:
        raise Exception('Divisor cannot be 0')
    result = a//b
    remainder = a%b
    print(a, '/', b, 'is', result, 'remainder', remainder)
    print('not possible')
    
remainer_division(21, 7)
remainer_division(13, 5)
remainer_division(90, 0)
remainer_division(0, 78)
remainer_division(9, 4)