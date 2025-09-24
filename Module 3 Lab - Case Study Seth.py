class Vehicle:
    def __init__(self, make, model, year, doors, roof):
        self.make = make
        self.model = model
        self.year = year
        self.doors = doors
        self.roof = roof

    def describe_car(self):
        print(F"Make : {self.make} \n"
              F"Model : {self.model} \n"
              F"Year : {self.year} \n"
              F"Doors : {self.doors} \n"
              F"Roof : {self.roof}")
make = input("Enter make: ")
model = input("Enter model: ")
year = input("Enter year: ")
doors = input("Enter doors: ")
roof = input("Enter roof: ")
vehicle = Vehicle(make, model, year, doors, roof)
vehicle.describe_car()