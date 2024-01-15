"""
    Виконавець: Олександр Яценко
    Homework V - Група вимог I

    Цей скрипт виконує гру FizzBuzz у заданому діапазоні чисел від користувача.

    Пакетні версії:
    pip - v23.3.1
"""


class FizzBuzzGame:
    def __init__(self, num_start: int, num_end: int) -> None:
        self.num_start = num_start
        self.num_end = num_end

    def play_game(self):
        fizz_buzz = []

        if self.num_start != 0 and self.num_end > self.num_start:
            for i in range(self.num_start, self.num_end + 1):
                if i % 3 == 0 and i % 5 == 0:
                    fizz_buzz.append("FizzBuzz")
                elif i % 3 == 0:
                    fizz_buzz.append('Fizz')
                elif i % 5 == 0:
                    fizz_buzz.append('Buzz')
                else:
                    fizz_buzz.append(i)

        return fizz_buzz
