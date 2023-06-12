# inheritance class

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return "The engine is running."


class Car(Vehicle):
    def start_engine(self):
        return super().start_engine() + " " + "It is a car engine."


his_car = Vehicle("Toyota", 'Corolla', 2020)
my_car = Car("Toyota", 'Corolla', 2020)

print(his_car.start_engine())
print(my_car.start_engine())
