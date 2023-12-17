# An example from the Internet (since there are no programming skills yet)
import numpy as np

array = np.array([1, 2, 3, 4, 5])

squared_array = array ** 2

# The code is written by me
user_number_one = int(input('Введіть перше позитивне ціле число: '))
user_number_two = int(input('Введіть друге ціле позитивне число: '))

result = user_number_one + user_number_two


if __name__ == '__main__':
    print('\n##### RESULTS #####\n')
    print('Результат обчислення вводу користувача:', result)
    print('Результат обчислення бібліотеки NumPy:', squared_array)
    print('Поточна версія NumPy:', np.__version__)
