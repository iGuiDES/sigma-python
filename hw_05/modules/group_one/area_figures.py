"""
    Виконавець: Олександр Яценко
    Homework V - Група вимог I

    Цей скрипт дозволяє користувачу обрати між розрахунком площі
    круга чи прямокутника.

    Пакетні версії:
    pip - v23.3.1
"""


class ShapeAreaCalculator:
    @staticmethod
    def calculate_circle_area(radius: str) -> float | str:
        try:
            if float(radius) < 0:
                raise ValueError('Радіус не може бути відʼємним.')
            else:
                return round(3.14 * float(radius) ** 2, 2)
        except ValueError as ve:
            return f'Помилка введення даних: {ve}'

    @staticmethod
    def calculate_rectangle_area(length: float, width: float) -> float | str:
        try:
            if float(length) < 0 or float(width) < 0:
                raise ValueError("Довжина і ширина не можуть бути від'ємними")
            else:
                return float(length) * float(width)
        except ValueError as ve:
            return f'Помилка введення даних: {ve}'
