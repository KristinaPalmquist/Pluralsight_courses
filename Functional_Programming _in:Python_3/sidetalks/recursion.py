
# def s(n):
#     if n == 0:
#         return n
#     else:
#         return n + s(n - 1)
    
# # import sys
# # # print(sys.getrecursionlimit())
# # # sys.setrecursionlimit(10000)
# print(s(10))


# # tail recursive
# def s2(n, acc=0):
#     if n == 0:
#         return acc
#     else:
#         return s2(n - 1, acc + n)
   
# print(s2(10))


# trampolining
# import types

# def tramp(gen, *args, **kwargs):
#     g = gen(*args, **kwargs)
#     while isinstance(g, types.GeneratorType):
#         g = next(g)
#     return g


def f(n, curr=0, next=1):
    if n == 0:
        return curr
    else:
        return f(n -1, next, curr + next)
    
print([f(i) for i in range(100)])


# from tramp import 

# def f2(n, curr=0, next=1):
#     if n == 0:
#         yield curr
#     else:
#         yield f2(n -1, next, curr + next)
# print([tramp(f2, i) for i in range(10)])