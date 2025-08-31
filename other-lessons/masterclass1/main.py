# Master Class OOP & Magic Methods

from abc import ABC, abstractmethod

# -----------------------------
# Абстрактный класс Vehicle
# -----------------------------
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# -----------------------------
# Класс Car (наследует Vehicle)
# -----------------------------
class Car(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} started!")

    def stop(self):
        print(f"{self.brand} {self.model} stopped!")

    # Магический метод для вывода объекта
    def __str__(self):
        return f"Car: {self.brand} {self.model}"

    # Магический метод для сложения двух машин (например, суммируем мощность)
    def __add__(self, other):
        return f"{self.brand} + {other.brand} combination"

# -----------------------------
# Класс Truck (наследует Car)
# -----------------------------
class Truck(Car):
    def __init__(self, brand, model, load_capacity):
        # self.brand = brand
        # self.model = model
        super().__init__(brand, model) # вызывает Car.__init__
        self.load_capacity = load_capacity

    def __str__(self):
        return f"Truck: {self.brand} {self.model}, Load: {self.load_capacity}kg"

# -----------------------------
# Пример работы кода
# -----------------------------
def main():
    # Создаем объекты
    car1 = Car("Toyota", "Camry")
    car2 = Car("Honda", "Civic")
    truck1 = Truck("Volvo", "FH", 20000)

    # Работа методов
    car1.start()
    car2.start()
    truck1.start()

    car1.stop()
    truck1.stop()

    # Магические методы
    print(car1)           # __str__
    print(truck1)         # __str__
    print(car1 + car2)    # __add__

if __name__ == "__main__":
    main()
