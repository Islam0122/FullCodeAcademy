import pyttsx3

engine = pyttsx3.init()

class Car:
    def __init__(self, brand):
        self.brand = brand

    def sound(self):
        return f"{self.brand} издает звук двигателя!"

class SportsCar(Car):
    def sound(self):
        return f"{self.brand} ревет: Вруум-вруум!"

class Truck(Car):
    def sound(self):
        return f"{self.brand} гудит: Бруум-бруум!"

# Создаем машины
cars = [SportsCar("Ferrari"), Truck("Volvo")]

for car in cars:
    msg = car.sound()
    print(msg)
    engine.say(msg)
    engine.runAndWait()
