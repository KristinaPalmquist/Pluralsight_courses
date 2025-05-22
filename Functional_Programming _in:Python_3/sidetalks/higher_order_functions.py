
""" HIGHER ORDER FUNCTIONS IN PYTHON """


""" COMPOSITION """
# def f(x):
#     return x+2

# def g(h, x):
#     return h(x) *2

# print(f(42))
# print(g(f, 42)) # function composition - writing a new function using other functions


""" CLOSURE """
# def addx(x): 
#     def _(y): # throwaway function, takes the value of x and throws to the outer function
#         return x + y
#     return _ # new function is returned as a result of the outer function

# add2 = addx(2) # define new function, which adds 2 to any value passed in
# add3 = addx(3)
# print(add2) # returns a function object
# print(add2(2), add3(3), add2(4), add3(4)) # 4 6 6 7


""" CURRYING """
def f(x, y):
    return x*y

def f2(x):
    def _(y):
        return f(x,y)
    return _
    
print(f2(2)) # returns a reference to a function object
print(f2(2)(3)) # 6