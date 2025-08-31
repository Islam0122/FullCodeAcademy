
# 🐍— OOP Notes

## 1. Классы и объекты
- **Класс** — шаблон для создания объектов  
- **Объект** — экземпляр класса  

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Camry")
````

---

## 2. Атрибуты и методы

* **Атрибуты** — свойства объекта
* **Методы** — функции объекта

```python
class Car:
    def start(self):
        print("Car started!")

my_car.start()
```

---

## 3. Наследование

* Создание нового класса на основе существующего

```python
class Vehicle:
    def __init__(self, name):
        self.name = name

class Car(Vehicle):
    def honk(self):
        print("Beep!")
```

---

## 4. Абстрактные классы

* **Нельзя создавать объекты напрямую**
* Подклассы **обязаны реализовать методы**

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started!")
```

---

## 5. Инкапсуляция

* Скрытие внутренних данных и методов
* Приватные атрибуты через `_` или `__`

```python
class Car:
    def __init__(self, brand):
        self.__brand = brand  # приватный атрибут
    def get_brand(self):
        return self.__brand
```

---

## 6. Полиморфизм

* Одинаковый интерфейс для разных объектов

```python
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

for animal in [Dog(), Cat()]:
    animal.speak()
```

---

## 7. Магические методы

* Специальные методы `__method__`
* Делают объекты удобными и питоничными

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"Car: {self.brand}"

my_car = Car("Toyota")
print(my_car)  # Car: Toyota
```

* Примеры: `__init__`, `__str__`, `__add__`, `__len__`, `__getitem__`, `__call__`



