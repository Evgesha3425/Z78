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
    def __init__(self):
        self.Air = Air()
        self.Railway = Railway()
        self.Automobile = Automobile()

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

    CITIES = {
        "Minsk": [["Warsaw", 476], ["Kiev", 417]],
        "Warsaw": [["Minsk", 476], ["Kiev", 690]],
        "Kiev": [["Minsk", 417], ["Warsaw", 690]]
    }

    def distance(self, city1, city2):
        for c1 in Agency.CITIES:
            if c1 == city1:
                for c2 in Agency.CITIES[c1]:
                    if c2[0] == city2:
                        return c2[1]

    def choose_transport(self):
        city1 = input("Укажите откуда хотите отправлять товар: ")
        city2 = input("Укажите куда хотите отправлять товар: ")
        print("-------------------")
        print(f"Отправка товара из {city1} в {city2} возможна следующими путями:")

        if city1 in self.BIG_CITIES and city2 in self.BIG_CITIES:
            print(f"Air. Цена за 1 кг товара составит {self.Air.PRICE_PER_KILO} $.")
            print(f"Railway. Цена за 1 кг товара составит {self.Railway.PRICE_PER_KILO} $.")
            print(f"Automobile. Цена за 1 кг товара составит {self.Automobile.PRICE_PER_KILO} $.")

        elif city1 in Agency.MEDIUM_CITIES and city2 in Agency.MEDIUM_CITIES:
            print(f"Railway. Цена за 1 кг товара составит {self.Railway.PRICE_PER_KILO} $.")
            print(f"Air. Цена за 1 кг товара составит {self.Air.PRICE_PER_KILO} $.")

        else:
            print(f"Automobile. Цена за 1 кг товара составит {self.Automobile.PRICE_PER_KILO} $.")

        print("-------------------")
        transport = input("Каким путем вы хотели бы отправить Ваш товар?: ")

        if transport == "Air":
            return self.Air.info(city1, city2)
        if transport == "Railway":
            return self.Railway.info(city1, city2)
        if transport == "Automobile":
            return self.Automobile.info(city1, city2)


class Transport:
    def time_of_delivery(self, city1, city2):
        return Agency.distance(Agency, city1, city2) / self.SPEED

    def weight(self):
        return int(input("Введите вес товара в килограммах: "))

    def price(self, weight, distance):
        return weight * self.PRICE_PER_KILO * distance

    def info(self, city1, city2):
        print(f"Расстояние составит {Agency.distance(Agency, city1, city2)} км,"
              f"стоимость пересылки составит {self.price(self.weight(), Agency.distance(Agency, city1, city2))} $, "
              f"время в пути составит {self.time_of_delivery(city1, city2)} часа")


class Air(Transport):
    SPEED = 300  # средняя скорость движения самолета
    PRICE_PER_KILO = 27.35  # стоимость за единицу веса на 1 км пути


class Railway(Transport):
    SPEED = 80  # средняя скорость движения поезда
    PRICE_PER_KILO = 12.44  # стоимость за единицу веса на 1 км пути


class Automobile(Transport):
    SPEED = 100  # средняя скорость движения автомобиля
    PRICE_PER_KILO = 8.28  # стоимость за единицу веса на 1 км пути


def greetings():
    print("Добрый день! Приветствуем Вас с нашей компании!")
    name = input("Подскажите, пожалуйста, как к Вам можно обращаться? ")
    print(f"Рады знакомству, {name}! Компания DPD занимается грузоперевозками и имеет 9 филиалов в 3-х странах.")
    print("-------------------")


    DPD = Agency()
    DPD.choose_transport()


greetings()



