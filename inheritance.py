class Vehicle:
    def general_usage(self):
        print("general use: transportation")

class Car(Vehicle):
    def __init__(self):
        print("i am car")
        self.wheels=4
        self.has_roof =True

    def specific_usage(self):
        print("specific use: commute to work")

class MotorCycle(Vehicle):
    def __init__(self):
        print("i am motor cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("specific use: road trips")


c=Car()


m=MotorCycle()



print(isinstance(m,Car))
print(issubclass(Car,Vehicle))