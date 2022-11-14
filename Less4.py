# def summa(*args):
#     total = 0
#     for i in args:
#         total += i
#     return 1
#
#
# print(summa(1, 2, 3))


# def is_year_leap(year):
#     if (year % 4 == 0 and year % 100) or year % 400 == 0:
#         return True
#     else:
#         return False
#
#
# print(is_year_leap(2600))


# def season(month):
#     if month in [12, 1, 2]:
#         return 'зима'
#     elif month in [3, 4, 5]:
#         return 'весна'
#     if month in [6, 7, 8]:
#         return 'лето'
#     else:
#         return 'осень'
#
#
# print(season(int(input('Введите номер месяца: '))))


# def factorial(n):
#     if n != 0:
#         return n * factorial(n-1)
#     else:
#         return True
#
#
# print(factorial(5))


# def razrad(n):
#     counter = 0
#     while n != 0:
#         counter += 1
#         n //= 10
#     return counter
#
#
# n = int(input('Введите число: '))
# print(razrad(n))


# def foo(*args, **kwargs):
#     for i in range(1, len(args)+1, 2):
#         print(args[i], end=' ')
#     print()
#     for value in kwargs.values():
#         if type(value) is str:
#             print(value, end=' ')
#
#
# foo(1, 2, 3, 7, 8, 9, a =4, b='5', c='6', d=10, e=11, f=12)