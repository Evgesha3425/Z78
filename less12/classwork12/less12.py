"""
ООП
"""


# 1
# class Animal:
#     FEET = 4  # статическая переменная (статический аргумент)
#
#     # метод экземпляра класса
#     def say(self, voice):  # self - гооворит о том, что метод принадлежит конкретному классу (указывает на текущий экземпляр класса)
#         print(f"I say {voice}")
#
#     def info_feet(self):
#         print(f"I have {Animal.FEET}")
#
#
# tom = Animal()  # tom представляет экземпляр класса
# bobik = Animal()  # bobik тоже будет экземпляром класса
#
# tom.say("meow")
# bobik.say("gav")


# 2
# сеттер - функция, которая передает значение аргумента
# class Human():
#     def __init__(self, name: str, age: int, cash: int = 2000):  # Конструктор класса
#         self.name = name
#         self.age = age
#         self.cash = cash
#
#     def info(self):
#         print(f"name: {self.name}, age: {self.age}")
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_age(self, age):
#         self.age = age
#
#     def after_year(self):
#         self.age += 1
#         self.info()
#
#
# Mark = Human("Mark", 28)
# for i in range(5):
#     Mark.after_year()


# class Person(object):
#     def __init__(self, name, age, passport_id, iban):
#         self.name = name  # публичное поле (public)
#         self.age = age  # публичное поле
#         self._passport_id = passport_id  # защищенное поле (protected)
#         self.__iban = iban  # приватное поле (private)
#
#     def info(self):
#         print(f"name {self.name}, age {self.age}")
#
#     def get_password_id(self):
#         return self._passport_id
#
#     def get_iban(self):
#         return self.__iban
#
#     @staticmethod  # статичный метод, служит для описания функции внутри класса
#     def weather(temperature, obj):
#         if temperature <= -5:
#             print(f"{obj.name} wear cap")
#         else:
#             print(f"{obj.name} wear jacket")
#
#     @classmethod
#     def create_object(cls):  # cls - ссылка на сам класс. Такой метод, который принадлежит классу и используется для создания экземпляра
#         name = input("enter name: ")
#         age = input("enter age: ")
#         passport_id = int(input("enter passport_id: "))
#         iban = int(input("enter iban: "))
#         human = cls(name, age, passport_id, iban)
#         return human
#
#
# class Worker(Person):
#     def __init__(self, name, age, passport_id, iban, work_time):
#         Person.__init__(self, name, age, passport_id, iban)
#         self.work_time = work_time
#
#     def get_money(self):
#         print(f"I work and do nothing and I have 2000 $")
#
#     def info_worker(self):
#         self.info()
#         print(f"I work {self.work_time} years")
#         print(f"passport_id {self._passport_id}")
#         print(f"iban {self.get_iban()}")
#
#
# Poul = Person("Poul", 28, 82149879832749, 1242389)
# Tom = Worker("Tom", 25, 236326523, 7536434, 9)
# Tom.get_money()
# Tom.info_worker()

# Инкапсуляция
# Инкапсуляция - есть такие методы (поля класса), которые должны быть скрыты от внешнего воздействия - логика, которая должна быть защищена от воздействия


# class Shop(object):
#     def __init__(self, goods={}):
#         self.goods = goods
#
#     def info(self):
#         for good, costs in self.goods.items():
#             print(good, costs)
#         print("-------------")
#
#     def check_goods(self, good):
#         return good in self.goods
#
#     def add_good(self, good, costs):
#         if self.check_goods(good):
#             print(f"The costs was changed. {good} is {costs} now")
#         self.goods[good] = costs
#
#     def del_good(self, good):
#         if self.check_goods(good):
#             del self.goods[good]
#             print(f"{good} was delete")
#         else:
#             print(f"{good} not in our shop")
#
#
#
# GOODS = {
#     "Milk": 2.52,
#     "Cheese": 18.24,
#     "Water": 1.45,
#     "Tomato": 12.53,
#     "Potato": 2.52
# }
#
# evroopt = Shop(GOODS)
# evroopt.info()
# evroopt.add_good("Tomato", 14.29)
# evroopt.add_good("Bread", 1.53)
# evroopt.add_good("Banana", 4.99)
# evroopt.info()
# evroopt.del_good("Melon")
# evroopt.info()