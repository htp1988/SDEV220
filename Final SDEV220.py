import pandas as pd


class UsedCar:
    def __init__(self, make=None, model=None, color=None, year=None, mileage=None, price=None):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage
        self.price = price

    @classmethod
    def add_car(cls):
        cars = UsedCar()
        used_car_file = open('UsedCar.txt', 'a')  # open file to append, create file if not exist
        make = input("Enter make: ")
        model = input("Enter model: ")
        color = input("Enter color: ")
        year = input("Enter year: ")
        mileage = input("Enter mileage: ")
        price = input("Enter price: ")

        car = UsedCar(make, model, color, year, mileage, price)
        car_info = [car.make, car.model, car.color, car.year, car.mileage, car.price]

        for i in car_info:
            used_car_file.write("%s\t" % i)
        used_car_file.write("\n")
        used_car_file.close()
        print("Successfully add to the inventory.")

    def set_make(self, make):  # set self.make to make (user input)
        self.make = make

    def get_make(self):  # return make value from user input
        return self.make

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_mileage(self, mileage):
        self.mileage = mileage

    def get_mileage(self):
        return self.mileage

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


class Buyer:
    def __init__(self, name, price_range, car_type):
        self.name = name
        self.priceRange = price_range
        self.carType = car_type


c1 = UsedCar()
c1.add_car()


