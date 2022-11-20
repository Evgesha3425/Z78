"""
1. Реализуйте класс MoneyBox, для работы с виртуальной копилкой. Каждая копилка имеет ограниченную вместимость,
которая выражается целым числом – количеством монет, которые можно положить в копилку. Класс должен поддерживать
информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в копилку и узнавать, можно ли
добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.
"""


# class MoneyBox:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#
#     def info(self):
#         print(f"В копилкe поместится еще {self.capacity} монет")
#
#     def can_add(self, v):
#         if v <= self.capacity:
#             return False
#         else:
#             return True
#
#     def add(self, v):
#         if self.can_add(v) is True:
#             return self.capacity - v
#         else:
#             print("Уже не влазит :(")
#
#
# my_box = MoneyBox(100)
#
# my_box.info()
# my_box.add(5)
# my_box.info()


"""
2. Создать базовый класс «сотрудник» и производные классы «стажер», «работник», «начальник отдела», «директор». 
Выведите на экран целое число – уровень допуска, вещественное число – зарплату и название должности.
"""


# class Employees:
#     def __init__(self, level: int, salary: float, position: str):
#         self.level = level
#         self.salary = salary
#         self.position = position
#
#     def print_info(self):
#         print("------------")
#         print(f"Уровень допуска: {self.level}")
#         print(f"Зарплата: {self.salary}")
#         print(f"Должность: {self.position}")
#         print("------------")
#
#
# class Trainee(Employees):
#     def __init__(self, level: int, salary: float, position: str):
#         Employees.__init__(self, level, salary, position)
#
#
# class Employee(Employees):
#     def __init__(self, level: int, salary: float, position: str):
#         Employees.__init__(self, level, salary, position)
#
#
# class Head_of_departmen(Employees):
#     def __init__(self, level: int, salary: float, position: str):
#         Employees.__init__(self, level, salary, position)
#
#
# class director(Employees):
#     def __init__(self, level: int, salary: float, position: str):
#         Employees.__init__(self, level, salary, position)
#
#
# Max = Trainee(1, 565.5, "Стажер")
# Denis = Employee(2, 763.9, "Работник")
# Kirill = Head_of_departmen(3, 1250.2, "Начальник отдела")
# Anna = director(4, 2500.0, "Директор")
#
# Max.print_info()
# Anna.print_info()


"""
3. Создать базовый класс «Грузоперевозчик» и производные классы «Самолет», «Поезд», «Автомобиль». Определить время и 
стоимость перевозки для указанных городов и расстояний
"""


# class Trucking:
#     def __init__(self, target: str, distance: float):
#         self.target = target
#         self.distance = distance
#
#
# class Airplane(Trucking):
#     SPEED = 300
#
#     def __init__(self, target, distance):
#         Trucking.__init__(self, target, distance)
#
#     def time(self):
#         return self.distance / self.SPEED
#
#     def info(self):
#         print(f"До {self.target} доберемся на {self.__class__.__name__} за {self.time}")
#
#
#
# Airplane.info("Санкт-Петербург", 980)


"""
4. Задача на взаимодействие между классами. Разработать систему «Интернет-магазин». Товаровед добавляет информацию 
о Товаре. Клиент делает заявку на товар, если товар есть в наличие в магазине то покупатель оплачивает товар иначе 
товаровед делает запрос на склад о наличии товара.
"""


class Shop:
    def __init__(self, good):
        self.good = good


class Stock(Shop):
    def __init__(self, good):
        Shop.__init__(self, good)

    def check_goods(self, good):
        return good in self.goods

    def add_good(self, good):
        if self.check_goods(good):
            print(f"The costs was changed. {good} is {costs} now")
        self.goods[good] = costs


class Product(Shop):
    def __init__(self, good):
        Shop.__init__(self, good)


