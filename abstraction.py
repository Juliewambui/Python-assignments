from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def __init__(self,model,engine, color):
        self.model = model
        self.engine = engine
        self.color = color

    def start_engine(self):
        return "Car engine started!"

    my_car = Car("subaru", 12345, "Red") 
    #my_vehicle = Vehicle()
    print(my_Car.start_engine()) 