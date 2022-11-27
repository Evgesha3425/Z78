# class Figure:
#     COLOR = "red"
#
#
# class Rectangle(Figure):
#     COLOR = "orange"
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def square(self):
#         return self.a * self.b
#
#     def perimetr(self):
#         return 2 * (self.a + self.b)
#
#
# class Circle(Figure):
#     COLOR = "blue"
#
#     def __init__(self, r):
#         self.r = r
#
#     def square(self):
#         return 3.14 * self.r ** 2
#
#     def perimetr(self):
#         return 2 * 3.14 * self.r
#
#
# class Summa:
#     def summa(self, a, b=None):
#         if b is None:
#             return a
#         else:
#             return a + b
#
#
# summ = Summa()
# print(summ.summa(1, 6))


# circle = Circle(5)


# rect1 = Rectangle(1, 2)
# rect2 = Rectangle(3, 4)
# circle1 = Circle(5)
# circle2 = Circle(2)
#
# figure = [rect1, rect2, circle1, circle2]
#
# for fig in figure:
#     print(f"S = {fig.square()}")
#     print(f"P = {fig.perimetr()}")


# class Person:
#     def __init__(self, name, age):
#         print("I'm worker")
#         self.age = age
#         self.name = name
#
#     def info(self):
#         print(f"name: {self.name}, age: {self.age}")
#
#
# class Worker:
#     def info(self, company):
#         super().info()
#         self.company = company
#         print(f"I work in {self.company}")
#
#
# class Manager(Worker, Person):
#     def __init__(self, name, age, id):
#         super().__init__(name, age)
#         print("I'm manager")
#         self.id = id
#
#     def info(self):
#         super().info("Apple")
#         print(f"id: {self.id}")
#
#
# Vasya = Manager("Vasya", 25, 5)
# Vasya.info()


# from abc import ABC, abstractmethod
#
#
# class Weapon(ABC):
#     @abstractmethod
#     def shoot(self):
#         print("use something")
#
#
# class Gun(Weapon):
#     def shoot(self):
#         print("bah")
#
#
# class Automat(Gun):
#     def shoot(self):
#         print("bah bah bah")
#
#
# class Knife(Weapon):
#     def shoot(self):
#         print("wjoooh")
#
#
# class RPG(Weapon):
#     def shoot(self):
#         print("badabum")
#
#
# Tokarev = Gun()
# Tokarev.shoot()
#
# AK_47 = Automat()
# AK_47.shoot()
#
# knife = Knife()
# knife.shoot()
#
# weapon = Weapon()
# weapon.shoot()


# class Human(object):
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property
#     def old(self):
#         return f"age: {self._age}"
#
#     @old.setter
#     def old(self, age):
#         self._age = age
#
#     # @old.deleter
#     # def old(self):
#     #     del self._age
#     #     print("deliter work")
#
# Vasya = Human("Vasya", 24)
# Vasya.old = 27
# del Vasya.old
# print(Vasya.old)



# class Human(object):
#     def __new__(cls, *args, **kwargs):
#         print("new work")
#         return super().__new__(cls)
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     def __str__(self):
#         return f"class: {self._name}"
#
#     def __repr__(self):
#         return f"class {Human} name {self._name}"
#
#
# Vasya = Human("Vasya", 25)
# print(repr(Vasya))


def greeting():
    return "hello python"


A = type("Point", (), {"MAX_VALUE": 100, "MIN_VALUE": 0, "greeting": lambda: "hello python"})
print(A.greeting())