# def summa(x: int, y: int) -> int:
#     return x ** y
#
# print(summa(6, 3))


# def maximum(numb1, numb2):
#     if numb1 > numb2:
#         return numb1
#     else:
#         return numb2


# a1, b1 = map(int, input().split())
# a2, b2 = map(int, input().split())
# print(maximum(maximum(a1, b1), maximum(a2, b2)))


# lst = [int(i) for i in input().split()]
# max_value = lst[0]
# for elem in lst:
#     max_value = maximum(elem, max_value)
#
# print(max_value)


#  АНАНОМНЫЕ ФУНКЦИИ
# def foo():
#     pass
#
# def foo2():
#     pass
#
# lst = [foo, foo2]
# for fun in lst:
#     fun()


# def power(x):
#     return x ** 2


# lst = [6, 3, 6, 2, 1, 6, 5, -5, 6, 1, 2]
# workers = {
#     "Poul": 1400,
#     "Mike": 7000,
#     "Kate": 890,
#     "Tom": 2500,
#     "Alice": 2010
# }

# print(list(map(lambda x: x**2, lst)))
# print([i**2 for i in lst])
#
# lst.sort(key=lambda x: -x % 2, reverse=True)
# print(lst)


# f = lambda x: x ** 2
# print(f(9))


# bomond = list(filter(lambda x: int(workers[x]) > 2000, workers))
# for worker in workers:
#     if worker not in bomond:
#         workers[worker] += 200


# premia = {worker: workers[worker]+200 for worker in workers if
#           worker not in list(filter(lambda x: int(workers[x]) > 2000, workers))}
# print(workers)


# new_lst = list(map(lambda x: x // 2, lst))
# print(new_lst)

# legb
# local
# enclosing  (замыкающая область)
# global
# build it
# замыкание
# def creator(x):
#     def inner(var_a):
#         nonlocal x
#         x += var_a
#         return x
#
#     return inner
#
# fun = creator(7)
# print(fun(3))
# print(fun(4))


# def decorator(fun):
#     def inner(a, b):
#         result = fun(a, b)
#         return result ** 2
#
#     return inner
#
#
# @decorator
# def summa(a, b):
#     return a + b
#
#
# # print(summa(2, 3))
# # summa = decorator(summa)
# print(summa(2, 3))


# from functools import wraps
# workers = {
#     'Tom': 2500,
#     'Mike': 4000,
#     'Alice': 1500,
#     'Vanya': 1000,
# }
#
# def deccorator(fun):
#     @wraps(fun)
#     def inner(*args, **kwargs):
#         result = fun(*args, **kwargs)
#         if result >= 10000:
#             for person in kwargs:
#                 kwargs[person] += kwargs[person] * 0.05
#             return kwargs
#         else:
#             return f'we have not money in our company'
#     return inner
#
# @deccorator
# def viplaty(*args, **kwargs):
#     return sum(kwargs.values())
#
#
# print(viplaty(**workers))

# рекурсия - функция, вызывающая внутри себя саму себя
#

# def foo():
#     print("It's fun foo")
#     foo()
#
# foo()

# def factorial(number):
#     if number == 1:
#         return 1
#     else:
#         return number * factorial(number - 1)
#
# print(factorial(5))


# def is_power(n):
#     if n ==1:
#         return True
#     elif n % 2 == 0:
#         return is_power(n // 2)
#     else:
#         return False
#
#
# print(is_power(2048))
# объявление функции
from math import sqrt
# объявление функции
def solve(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = ((-b + sqrt(D)) / (2 * a))
        x2 = ((-b - sqrt(D)) / (2 * a))
    else:
        print((-b) / (2 * a))
    return x2, x1

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)