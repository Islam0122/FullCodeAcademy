
---

## **1. Классы и объекты**

* **Класс** — это “шаблон” для создания объектов.
* **Объект** — конкретный экземпляр класса.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

my_car = Car("Volvo")
```

---

## **2. Наследование**

* Позволяет **создавать новый класс на основе существующего**.
* Подкласс наследует все свойства и методы базового класса.

```python
class SportsCar(Car):
    def speed(self):
        return "Быстрая машина"
```

---

## **3. Полиморфизм**

* **Один метод, разные реализации** в разных классах.

```python
class Truck(Car):
    def sound(self):
        return "Грузовик гудит: Бруум-бруум!"

class SportsCar(Car):
    def sound(self):
        return "Спорткар ревет: Вруум-вруум!"

cars = [SportsCar("Ferrari"), Truck("Volvo")]
for car in cars:
    print(car.sound())  # Один метод, разные реализации
```

---

## **4. Инкапсуляция**

* **Скрытие внутренних данных** и контроль доступа через методы.
* В Python: `_attr` — защищённый, `__attr` — приватный.

```python
class Car:
    def __init__(self, brand):
        self.__brand = brand  # приватный

    def get_brand(self):
        return self.__brand

car = Car("Volvo")
print(car.get_brand())
```

---

## **5. Pyttsx3 для озвучивания**

* Библиотека для **текста в речь**.

```python
import pyttsx3
engine = pyttsx3.init()

engine.say("Привет, мир!")
engine.runAndWait()
```

* Можно использовать с объектами классов:

```python
engine.say(SportsCar("Ferrari").sound())
engine.runAndWait()
```

---

