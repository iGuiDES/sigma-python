"""
    Виконавець: Олександр Яценко
    Homework IV - Група вимог II

    Цей скрипт виконує гру FizzBuzz у заданому діапазоні чисел від користувача.
    Функція `fizz_buzz_game` приймає два параметри: початкове та кінцеве
    число діапазону, та повертає список з результатами гри FizzBuzz для
    цього діапазону.

    Пакетні версії:
    pip - v23.3.1
"""


def fizz_buzz_game(num_start, num_end):
    """
        Функція для виконання гри FizzBuzz у заданому діапазоні чисел.

        Args:
            num_start (int): Початкове число діапазону.
            num_end (int): Кінцеве число діапазону.

        Returns:
            list: Список з результатами гри FizzBuzz. Для кожного числа в
            діапазоні від `num_start`
            до `num_end` (включно), функція повертає:
                - "FizzBuzz", якщо число кратне і 3, і 5;
                - "Fizz", якщо число кратне тільки 3;
                - "Buzz", якщо число кратне тільки 5;
                - саме число, якщо воно не відповідає жодній із цих умов.
        """

    list_numbers = list()
    fizz_buzz = list()

    if num_start != 0 and num_end > num_start:
        for i in range(num_start, num_end + 1):
            list_numbers.append(i)

    if len(list_numbers) != 0:
        for i in list_numbers:
            if i % 3 == 0 and i % 5 == 0:
                fizz_buzz.append("FizzBuzz")
            elif i % 3 == 0:
                fizz_buzz.append('Fizz')
            elif i % 5 == 0:
                fizz_buzz.append('Buzz')
            else:
                fizz_buzz.append(i)

    return fizz_buzz
