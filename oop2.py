class House:
    def __init__(self, area, price):
        self.__area = area
        self.__price = price

    def final_price(self, discount : float):
        return self.__price * discount


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)


class Human:
    default_name = None
    default_age = 0
    def __init__(self, name = default_name, age = default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    # def __init__(self, name, age, money, house):
    #     self.name = name
    #     self.age = age
    #     self.__money = money
    #     self.__house = house
    def info(self):
        return self.name, self.age, self.__house, self.__money

    @classmethod
    def default_info(cls):
        return cls.default_name, cls.default_age

    def earn_money(self):
        self.__money += 1

    def __make_deal(self, house: House, price: int):
        self.__house = house
        self.__money -= price

    def buy_house(self, house : House, discount : float):
        final_price = house.final_price(discount)
        if final_price <= self.__money:
            self.__make_deal(house, final_price)
        else:
            print("Денег мало")


print(Human.default_info())
nata = Human("Nata", 33)
print(nata.info())
nata.earn_money()
print(nata.info())

small_house = SmallHouse(100)
nata.buy_house(small_house, 0.5)


for i in range(100):
    nata.earn_money()
print(nata.info())
nata.buy_house(small_house, 0.5)
print(nata.info())
