carList = []

class UsedCar:
    def __init__(self, id=None, make=None, model=None, color=None, year=None):
        self.id = id
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    # print out a cars attributes
    def __str__(self):
        return f'Car Info: {self.make} {self.model} {self.color} {self.year}'

    # add to the car list inventory as a dictionary structure
    def addCar(self):
        carList.append({'id': self.id, 'make': self.make, 'model': self.model, 'color': self.color, 'year': self.year})

    # save to file
    def save_to_file(self):
        car_info = [self.id, self.make, self.model, self.color, self.year]
        used_car_file = open('UsedCar.txt', 'a')
        for i in car_info:
            used_car_file.write("%s\t" % i)
        used_car_file.write("\n")
        used_car_file.close()
        print("Successfully add to the inventory.")

# Inventory/computer class
class Inventory:
    def __init__(self, searchValue=None):
        self.searchValue = searchValue

    def search(self):
        search_value = input("Make: ")
        if search_value is None or len(search_value) == 0:
            make_list = carList
        else:
            make_list = list(filter(lambda item: item["make"] == search_value, carList))
        print(make_list)

        search_value = input("Model: ")
        if search_value is None or len(search_value) == 0:
            model_list = make_list
        else:
            model_list = list(filter(lambda item: item["model"] == search_value, make_list))
        print(model_list)

        search_value = input("Color: ")
        if search_value is None or len(search_value) == 0:
            color_list = model_list
        else:
            color_list = list(filter(lambda item: item["color"] == search_value, model_list))
        print(color_list)

        search_value = input("Year: ")
        if search_value is None or len(search_value) == 0:
            year_list = color_list
        else:
            year_list = list(filter(lambda item: item["year"] == int(search_value), color_list))
        print(year_list)

    def set_search_value(self):
        self.searchValue = search_value

    def get_search_value(self):
        return self.searchValue

class Customer:
    def __init__(self, name, loanLength, price):
        self.name = name
        self.loanLength = loanLength
        self.price = price


# Used car objects
myCar1 = UsedCar('1', 'mazda', 'cx-7', 'purple', 2012)
myCar2 = UsedCar('2', 'ford', 'focus', 'white', 2015)
myCar3 = UsedCar('3', 'subaru', 'forester', 'black', 2018)
myCar4 = UsedCar('4', 'mazda', 'cx-5', 'black', 2020)
myCar5 = UsedCar('5', 'mazda', '6', 'black', 2018)
myCar6 = UsedCar('6', 'mazda', '6', 'white', 2019)

# methods on usedCars
myCar1.addCar()
myCar2.addCar()
myCar3.addCar()
myCar4.addCar()
myCar5.addCar()
myCar6.addCar()

# Inventory objects
search1 = Inventory()
search1.search()

# methods on Inventory

