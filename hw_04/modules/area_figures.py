"""
Виконавець: Олександр Яценко
Homework IV - Група вимог II

Опис програми: Цей скрипт дозволяє користувачу обрати між розрахунком площі
круга чи прямокутника.
За допомогою вводу користувача скрипт використовує функції для визначення та
виведення відповідної площі.
"""


def calculate_circle_area(radius: int):
    """
    Розрахунок площі круга за заданим радіусом.

    Args:
        radius (float): Радіус круга.

    Returns:
        float: Площа круга, заокруглена до двох знаків після коми.
    """
    try:
        if float(radius) < 0:
            raise ValueError('Радіус не може бути відʼємним.')
        else:
            return round(3.14 * int(radius) ** 2, 2)
    except ValueError as ve:
        return f'Помилка введення даних: {ve}'


def calculate_rectangle_area(length: float, width: float):
    """
    Розрахунок площі прямокутника за заданими довжиною та шириною.

    Args:
        length (float): Довжина прямокутника.
        width (float): Ширина прямокутника.

    Returns:
        float: Площа прямокутника.
    """
    try:
        if float(length) < 0 or float(width) < 0:
            raise ValueError(f"Довжина і висота не можуть бути від'ємними")
        else:
            return float(length) * float(width)
    except ValueError as ve:
        return f'Помилка введення даних: {ve}'
