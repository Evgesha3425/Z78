# class B:
#     pass
#
#
# class C:
#     pass


# A = type("Person", (B, C), {"MAX_VALUE": 100, "MIN_VALUE": 0})
# a = A()
# print(A.mro())

# class MetaPerson(type):
#     def __new__(cls, name, bases, dct):
#         dct.update({"MAX_VALUE":100, "MIN_VALUE: 0"})
#         return type.__new__(cls, name, bases, dct)
#
#     # def __init__(self, name, bases, dct):
#     #     super().__init__(name, bases, dct)
#     #     self.MAX_VALUE = 100
#     #     self.MIN_VALUE = 0
#
#
# class Person(metaclass=MetaPerson):
#     JOB = "merchendiser"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# person = Person("Vasya", 24)
# print(Person.__dict__)


# class Summatr:
#     def __init__(self, a):
#         self.a = a

    # def summa(self, other):
    #     if isinstance(other, int):
    #         return self.a + other
    #     elif isinstance(other, Summatr):
    #         return self.a + other.a
    #     else:
    #         raise TypeError("Type isn't correct")

    # def __add__(self, other):
    #     if isinstance(other, int):
    #         return self.a + other
    #     elif isinstance(other, Summatr):
    #         return self.a + other.a
    #
    # def __eq__(self, other):
    #     if isinstance(other, int):
    #         return self.a == other
    #     elif isinstance(other, Summatr):
    #         return self.a == other.a


# s1 = Summatr(6)
# s2 = Summatr(7)
# print(s1.__add__(s2))
# print(s1 + s2)
# print(s1 + s2)

# print(s1.__ne__(s2))


# """
# 2. Живое
# """
#
#
# from abc import ABC, abstractmethod
#
#
# class Alive(ABC):
#     COUNT = 0
#
#     @abstractmethod
#     def info_population(self):
#         return self.count
#
#
# class Plants(Alive):
#     def __init__(self, count, koef_grown):
#         self.count = count
#         self.koef_grown = koef_grown
#
#     def info_population(self):
#         return self.count
#
#     def year_after(self):
#         self.count *= self.koef_grown
#
#     def rabbits_food(self, rabbits):
#         self.count -= rabbits.count * 5
#
#
# class Rabbits(Alive):
#     def __init__(self, count, koef_rep):
#         self.count = count
#         self.koef_rep = koef_rep
#
#     def info_population(self):
#         return self.count
#
#     def year_after(self):
#         self.count *= self.koef_rep
#
#
# class Forest_boy():
#     def control(self, rabbits, plants):
#         return True if rabbits.count * 5 < plants.count else False
#
#     def is_add_plants(self, rabbits, plants):
#         if not self.control(rabbits, plants):
#             print("rabbits:", rabbits.count, "plants:", plants.count)
#             count_plants = int(input("How many plants add? "))
#             plants.count += count_plants
#
#
# plants = Plants(40, 10)
# rabbits = Rabbits(10, 5)
# Vasya = Forest_boy()
#
# year = 1
# while year < 10:
#     print("year:", year)
#     print("plants:", plants.info_population())
#     print("rabbits:", rabbits.info_population())
#     print("-------------")
#     rabbits.year_after()
#     plants.year_after()
#     plants.rabbits_food(rabbits)
#     Vasya.is_add_plants(rabbits, plants)
#     year += 1


# try:
#     print(5 + 7)
# except (TypeError, IndexError):
#     print("I catch type error or index error")
# except ZeroDivisionError:
#     print("Division by zero in ZeroDivisionError")
# except ArithmeticError:
#     print("Division by zero in ArithmeticError")
# else:
#     print("All good")
# finally:
#     print("Always work")


# def inner():
#     raise NotImplementedError


# def middle():
#     print("middle start work")
#     try:
#         print(inner())
#     except ValueError:
#         print("Middle catch ValueError")
#     print("middle end work")
#
#
# def senior():
#     print("senior start work")
#     try:
#         print(middle())
#     except IndexError:
#         print("Senior catch IndexError")
#     print("senior end work")
#
#
# senior()

# try:
#     print(inner())
# except NotImplementedError:
#     print("I catch NotImplementedError")
# except ValueError:
#     print("I catch ValueError")


# def login_github(password):
#     if len(password) < 5:
#         raise IndexError("password must be more then 4 sign")
#
#
# def after_login_github():
#     while True:
#         password = input("enter password: ")
#         try:
#             login_github(password)
#         except ValueError as error:
#             print("password not correct")
#             print(error.args)
#         else:
#             break
#
# try:
#     after_login_github()
# except IndexError:
#     print("we catch IndexError")




# class HaveNoMoney(Exception):
#     def __init__(self):
#         self.price = 25
#
#
# def shop(money):
#     print("buy cheese?")
#     if money < 25:
#         raise HaveNoMoney()
#     else:
#         print("Cheese bought")
#
#
# try:
#     money = int(input("enter money: "))
#     shop(money)
# except HaveNoMoney as error:
#     print(f"Сыр не купили. Нам не хватило на сыр {error.price - money}")
#     print(error.args)

# class CheeseNotFound(Exception):
#     pass
#
#
# class GaudaNotFound(CheeseNotFound):
#     pass
#
#
# def boy(money, name):
#     if money < 15:
#         raise NotImplementedError("Have no money")
#     elif name != "гауда":
#         raise CheeseNotFound
#     else:
#         return "cheese buy"
#
#
# def mother():
#     try:
#         print(boy(14, "гауда"))
#     except CheeseNotFound:
#         print("Сыр гауда не найден")
#     except NotImplementedError:
#         print("Не хватило денег")
#         raise
#
# mother()