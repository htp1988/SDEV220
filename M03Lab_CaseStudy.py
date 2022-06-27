class Vehicle:
    def __init__(self, vehicle_type=None):
        self.type = vehicle_type


class Car(Vehicle):
    def __init__(self,
                 vehicle_type=None,
                 year=None,
                 make=None,
                 model=None,
                 doors=None,
                 roof=None):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    @classmethod
    def add_car(cls):
        vehicle_type = input("Enter type of vehicle (Sorry, we just accept car now): ")

        if vehicle_type == "car" or vehicle_type == "Car":
            make = input("Enter make: ")
            model = input("Enter model: ")
            year = input("Enter year: ")
            doors = input("Enter number of doors: ")
            roof = input("Enter type of roof: ")

            car = Car(vehicle_type, make, model, year, doors, roof)
            print("\nYou are adding " + make + " " + model + " " + year + ", " + doors + " doors, " + roof)
            right = input("Is it right? (Y/N) ")

            if right == "Y" or right == "y":
                print("\nCar is added successfully. Below is car information:")
                print(car)

            else:
                print("\nFailed to add car.")

        else:
            print("Sorry, we just accept car type now.")

    def set_type(self):
        self.type = vehicle_type

    def get_type(self):
        return self.type

    def set_make(self):
        self.make = make

    def get_make(self):
        return self.make

    def set_model(self):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self):
        self.year = year

    def get_year(self):
        return self.year

    def set_doors(self):
        self.doors = doors

    def get_doors(self):
        return self.doors

    def set_roof(self):
        self.type = roof

    def get_roof(self):
        return self.roof

    def __str__(self):
        return "\nVehicle type: %s\n" \
               "Year: %s\n" \
               "Make: %s\n" \
               "Model:%s\n" \
               "Number of doors: %s\n" \
               "Type of roof: %s\n" \
               % (self.type, self.year, self.make, self.model, self.doors, self.roof)


def main():
    res = "Y"
    while res == "Y" or res == "y":
        car = Car()
        car.add_car()
        res = input("Do you want to continue? (Y/N) ")


main()
