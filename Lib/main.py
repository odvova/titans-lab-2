import random


class Person:
    def __init__(self, **kwargs):
        self.info = {
            'name': kwargs.get('name', " "),
            'age': kwargs.get('age', 0),
            'amount of money': kwargs.get('money', 0),
            'having house': kwargs.get('has_house', False)
        }


class Human(Person):
    def provide_info(self):
        print(str(self))

    def make_money(self, amount):
        self.info['amount of money'] += amount
        print(f"{self.info['name']} now has {self.info['amount of money']} money available.")

    def buy_house(self, house):
        if self.info['amount of money'] >= house.cost:
            self.info['amount of money'] -= house.cost
            self.info['having house'] = True
            print(f"{self.info['name']} has bought a house with an area of {house.area} sq. meters.")
        else:
            print(f"{self.info['name']} does not have enough money to buy this house.")

    def __str__(self):
        info_str = ""
        for key, value in self.info.items():
            info_str += f"{key}: {value}, "
        return info_str[:-2]


class House:
    def __init__(self, **kwargs):
        self.area = kwargs.get('area', 0)
        self.cost = kwargs.get('cost', 0)

    def apply_discount(self, discount):
        self.cost *= (1 - discount)


class Realtor:
    __instance = None

    def __init__(self, name, houses, discount):
        if Realtor.__instance is not None:
            raise Exception("Only one instance of Realtor is allowed!")
        else:
            self.name = name
            self.houses = houses
            self.discount = discount
            Realtor.__instance = self

    @staticmethod
    def get_instance():
        if Realtor.__instance is None:
            Realtor("John Doe", [], 0.0)
        return Realtor.__instance

    def provide_houses_info(self):
        print(f"{self.name} provides information about the following houses:")
        for house in self.houses:
            print(f"Area: {house.area}, Cost: {house.cost}")

    def give_discount(self, house):
        discount_amount = house.cost * self.discount
        discounted_price = house.cost - discount_amount
        print(f"{self.name} is giving you a discount of {self.discount * 100}% on this house. The discounted price is {discounted_price}.")

    def steal_money(self):
        if random.randint(1, 10) == 1:
            print(f"{self.name} has stolen your money!")
            return True
        return False


house1 = House(area=40, cost=258946)
human1 = Human(name="John", age=30, money=200000)
realtor1 = Realtor("William", [house1], 0.1)
realtor1.provide_houses_info()

human1.provide_info()
