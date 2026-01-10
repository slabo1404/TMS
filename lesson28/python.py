"""
1. Создайте класс "Круг", который имеет атрибуты радиус и цвет, и
методы вычисления площади и длины окружности. 
Создайте несколько объектов этого класса и вызовите его методы для каждого объекта.
"""

import math

class Circle:
    def __init__(self, radius, color=None):
        self.radius = radius
        self.color = color

    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    
    def calculate_circumference(self):
        return 2 * math.pi * self.radius

first_circle = Circle(3)
second_circle = Circle(10)

area = first_circle.calculate_area()
circumference = first_circle.calculate_circumference()

print(f"First circle has {area} area and {circumference} circumference")


"""
Создайте класс "Автомобиль", который имеет атрибуты марка, модель,
цвет и год выпуска. 
Создайте методы для получения и изменения этих атрибутов. 
Создайте несколько объектов этого класса и вызовите его методы для каждого
"""
    
class Vehicle:
    def __init__(self, brand, model, color, year):
        self._brand = brand
        self._model = model
        self._color = color
        self._year = year
    
    def get_brand(self):
        return self._brand
    
    def get_model(self):
        return self._model
    
    def get_color(self):
        return self._color
    
    def get_year(self):
        return self._year
    
    def set_brand(self, brand):
        self._brand = brand
    
    def set_model(self, model):
        self._model = model
    
    def set_color(self, color):
        self._color = color
    
    def set_year(self, year):
        self._year = year
    
    def print_attributes(self):
        print(f"{self._brand} {self._model} {self._color} {self._year}")
        

mazda = Vehicle("Mazda", "3", "green", 2010)
mazda.set_color("red")
mazda.set_year(2020)
mazda.print_attributes()