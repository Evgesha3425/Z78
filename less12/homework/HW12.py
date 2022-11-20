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
#             return True
#         else:
#             return False
#
#     def add(self, v):
#         if self.can_add(v) is True:
#             print(f"Ты добавил {v} монет")
#             print("---------")
#             self.capacity -= v
#         else:
#             print(f"{v} монет не влезет")
#
#
# my_box = MoneyBox(100)
#
# my_box.info()
# my_box.add(5)
# my_box.info()
# my_box.add(90)
# my_box.info()
# my_box.add(7)


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
#     def __init__(self, target: str, distance: float):
#         Trucking.__init__(self, target, distance)
#
#     def travel_time(self):
#         return self.distance / Airplane.SPEED
#
#     def info(self):
#         print(f"До {self.target} доберемся на {self.__class__.__name__} за {round(self.travel_time(), 2)} часов")
#
#
# class Train(Trucking):
#     SPEED = 90
#
#     def __init__(self, target: str, distance: float):
#         Trucking.__init__(self, target, distance)
#
#     def travel_time(self):
#         return self.distance / Train.SPEED
#
#     def info(self):
#         print(f"До {self.target} доберемся на {self.__class__.__name__} за {round(self.travel_time(), 2)} часов")
#
#
# class Automobile(Trucking):
#     SPEED = 120
#
#     def __init__(self, target: str, distance: float):
#         Trucking.__init__(self, target, distance)
#
#     def travel_time(self):
#         return self.distance / Automobile.SPEED
#
#     def info(self):
#         print(f"До {self.target} доберемся на {self.__class__.__name__} за {round(self.travel_time(), 2)} часов")
#
#
# way1 = Airplane("Мурманск", 1900)
# way2 = Train("Санкт-Петербург", 980)
# way3 = Automobile("Варшава", 780)
#
# way1.info()
# way2.info()
# way3.info()


"""
4. Задача на взаимодействие между классами. Разработать систему «Интернет-магазин». Товаровед добавляет информацию 
о Товаре. Клиент делает заявку на товар, если товар есть в наличие в магазине то покупатель оплачивает товар иначе 
товаровед делает запрос на склад о наличии товара.
"""


class Shop:
    def __init__(self, goods_in_shop):
        self.goods_in_shop = list(goods_in_shop)

    def info(self):
        print(self.goods_in_shop)


class Merchandiser(Shop):
    GOODS_IN_STOCK = ["monitor", "kettle", "iron", "TV", "mouse"]

    def __init__(self, goods_in_shop):
        self.goods_in_shop = list(goods_in_shop)

    def check_good_shop(self, good):
        return True if good in self.goods_in_shop else False

    def check_goods_stock(self, good):
        return True if good in Merchandiser.GOODS_IN_STOCK else False

    def add_good(self, good):
         print(f"Товар {good} уже в наличии в магазине") if self.check_good_shop(good) else self.goods_in_shop.append(good)


class Buyer:
    def find(self, good):
        if Merchandiser.check_good_shop(good):
            print("Товар в наличии в магазине, проходите оплачивайте на кассу")
        elif Merchandiser.check_goods_stock(good):
            print("Товар в наличии на складе") if True else print("Товара нет ни в магазине, ни на складе")


shop = Merchandiser([])

shop.add_good("TV")
shop.add_good("keyboard")
shop.add_good("mouse")
shop.add_good("SD-card")


Max = Buyer()
Max.find("TV")