"""
1. Разработайте программу, имитирующую работу транспортного агентства. Транспортное агентство имеет сеть филиалов в
нескольких городах. Транспортировка грузов осуществляется между этими городами тремя видами транспорта: автомобильным,
железнодорожным и воздушным. Любой вид транспортировки имеет стоимость единицы веса на единицу пути и скорость доставки.
Воздушный транспорт можно использовать только между крупными городами, этот вид самый скоростной и самый дорогой.
Железнодорожный транспорт можно использовать между крупными и средними городами, этот вид самый дешевый. Автомобильный
транспорт можно использовать между любыми городами. Заказчики через случайные промежутки времени обращаются в один из
филиалов транспортного агентства с заказом на перевозку определенной массы груза и возможным пожеланием о скорости/цене
доставки. Транспортное агентство организует отправку грузов одним из видов транспорта с учетом пожеланий клиента.

-Доход транспортного агентства, в том числе с разбивкой по видам транспорта и городам.
-Среднее время доставки груза, в том числе с разбивкой по видам транспорта и городам.
-Список исполняемых заказов с возможность сортировки по городам, видам транспорта, стоимости перевозки.
"""


class Agency:
    pass


    # def distance_railway(self, city1, city2):
    #     if city1 or city2 == "Минск" and city1 or city2 == "Warsaw":
    #         return 561
    #     if city1 or city2 == "Минск" and city1 or city2 == "Kiev":
    #         return 476
    #     if city1 or city2 == "Warsaw" and city1 or city2 == "Kiev":
    #         return 773
    #
    # def distance_automobile(self, city1, city2):
    #     if city1 or city2 == "Минск" and city1 or city2 == "Warsaw":
    #         return 546
    #     if city1 or city2 == "Минск" and city1 or city2 == "Kiev":
    #         return 525
    #     if city1 or city2 == "Warsaw" and city1 or city2 == "Kiev":
    #         return 780


class Air(Agency):
    SPEED_AIR = 300  # средняя скорость движения самолета
    PRICE_PER_KILO = 27.35

    def weight(self):
        return input("Введите вес товара в килограммах: ")

    def distance(self, city1, city2):
        if city1 or city2 == "Минск" and city1 or city2 == "Warsaw":
            return 476
        if city1 or city2 == "Минск" and city1 or city2 == "Kiev":
            return 417
        if city1 or city2 == "Warsaw" and city1 or city2 == "Kiev":
            return 690

    def price(self, weight: float, distance: float):
        return weight / distance  # цена за единицу веса на единицу пути

    def info(self):
        Air.distance(self.city1, self.city2)


# class Railway(Agency):
#     SPEED_RAILWAY = 80  # средняя скорость движения поезда
#
#     def __init__(self, weight, city1, city2):
#         super().__init__(weight, city1, city2)
#
#
# class Automobile(Agency):  # средняя скорость движения автомобиля
#     SPEED_AUTOMOBILE = 100
#
#     def __init__(self, weight, city1, city2):
#         super().__init__(weight, city1, city2)


BIG_CITIES = [  # большие города
    "Minsk",
    "Warsaw",
    "Kiev"
]
MEDIUM_CITIES = [  # средние города
    "Grodno",
    "Gdansk",
    "Donetsk"
]
SMALL_CITIES = [  # мелкие города
    "Slonim",
    "Bialystok",
    "Kherson"
]


def greetings():
    print("Добрый день! Приветствуем Вас с нашей компании!")
    name = input("Подскажите, пожалуйста, как к Вам можно обращаться? ")
    print(f"Рады знакомству, {name}! Компания DPD занимается грузоперевозками и имеет 9 филиалов в 3-х странах.")

    a = input("Укажите откуда хотите отправлять товар: ")
    b = input("Укажите куда хотите отправлять товар: ")
    print("-------------------")
    print(f"Отправка товара из {a} в {b} возможна следующими путями:")

    if a in BIG_CITIES and b in BIG_CITIES:
        print(f"Air. Цена за 1 кг товара составит {Air.PRICE_PER_KILO} $.")

    transport = input("Каким путем вы хотели бы отправить Ваш товар?: ")
    if transport == "Воздушный":
        return Air.info(a, b)


greetings()
DPD_agency_air = Air()


