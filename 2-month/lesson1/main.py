import pyttsx3

# Инициализация движка pyttsx3
engine = pyttsx3.init()

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} издает звук."

class Dog(Animal):
    def speak(self):
        return f"{self.name} говорит: Гав!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} говорит: Мяу!"

dog = Dog("Бобик")
cat = Cat("Мурка")

# Выводим текст и озвучиваем
for animal in [dog, cat]:
    message = animal.speak()
    print(message)
    engine.say(message)
    engine.runAndWait()