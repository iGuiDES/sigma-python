"""
    Виконавець: Олександр Яценко
    Homework II - 2 рівень складності

    Цей скрипт дозволяє користувачу обчислити площу кола або прямокутника
    залежно від їх вибору.

    Спочатку користувачу пропонується обрати, для якої фігури він хоче
    обчислити площу: кола або прямокутника.
    Вибір відбувається шляхом введення одного із двох рядків: "circle" або
    "rectangle".

    - Якщо вибрано "circle", користувачу пропонується ввести радіус кола.
    Скрипт перевіряє введене значення на коректність:
      воно не має бути від'ємним або пустим. Якщо введене значення валідне,
      обчислюється площа кола за формулою πr²
      (де π = 3.14), та результат виводиться.

    - Якщо вибрано "rectangle", користувачу пропонується ввести довжину та
    ширину прямокутника. Скрипт перевіряє обидва
      введені значення на коректність: вони не повинні бути від'ємними або
      пустими. Якщо введені значення валідні,
      обчислюється площа прямокутника за формулою довжина × ширина,
      та результат виводиться.

    У разі введення некоректних даних, скрипт виведе відповідне повідомлення
    про помилку.

    Package version:
    pip - v23.3.1
"""

circle_area = str()
rectangle_area = str()

user_answer = input(
    'Виберіть та введіть одне із значень в дужках ("circle", "rectangle"): '
)

if user_answer.lower() == 'circle':
    circle_radius = input('Введіть радіус кола: ')

    try:
        if int(circle_radius) < 0:
            raise ValueError('Радіус не може бути відʼємним.')
        elif circle_radius == '':
            raise ValueError("Надаль, Ви не можете ввести тут стрічку.")
        else:
            circle_area = 3.14 * float(circle_radius) * float(circle_radius)

    except ValueError as ve:
        print(f'Помилка введення даних: {ve}')

    except Exception as error:
        print(f'Помилка {error}')

    finally:
        print(circle_area)

if user_answer.lower() == 'rectangle':
    rectangle_length = input('Введіть довжину прямокутника: ')
    rectangle_width = input('Введіть висоту прямокутника: ')

    try:
        if int(rectangle_length) < 0:
            raise ValueError(f"Довжина не може бути {rectangle_length}")
        elif int(rectangle_width) < 0:
            raise ValueError(f"Висота не може бути {rectangle_width}")
        elif rectangle_width == '':
            raise ValueError("Значення не повинно бути пустими")
        elif rectangle_length == '':
            raise ValueError("Значення не повинно бути пустими")
        else:
            rectangle_area = int(rectangle_length) * int(rectangle_width)

    except ValueError as ve:
        print(f'Помилка введення даних: "{ve}"')

    except Exception as e:
        print(f'Помилка: "{e}"')

    finally:
        print(rectangle_area)
