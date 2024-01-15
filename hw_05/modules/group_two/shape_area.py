"""
    Виконавець: Олександр Яценко
    Homework V - Група вимог II

    Цей скрипт дозволяє користувачу обрати між розрахунком площі
    круга, прямокутника чи трикутника.

    Пакетні версії:
    pip - v23.3.1
"""

import math


class Shape:
    def calculate_area(self):
        raise NotImplementedError(
            "Метод calculate_area() потрібно реалізувати у підкласі."
        )


class Circle(Shape):
    def __init__(self, radius: int) -> None:
        self.radius = radius

    def calculate_area(self):
        if self.radius < 0:
            return 'Радіус не може бути відʼємним.'
        return round(math.pi * self.radius ** 2, 2)


class Rectangle(Shape):
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

    def calculate_area(self):
        if self.length < 0 or self.width < 0:
            return "Довжина і ширина не можуть бути від'ємними."
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base: int, height: int) -> None:
        self.base = base
        self.height = height

    def calculate_area(self):
        if self.base < 0 or self.height < 0:
            return "Основа та висота не можуть бути від'ємними."
        return 0.5 * self.base * self.height
