"""
Виконав: Олександр Яценко
Homework 1 - I рівень складності

Цей скрипт призначений для обчислення площ різних геометричних фігур: кола,
прямокутника та трикутника.

Опис:
- Спочатку користувач вводить необхідні розміри для кожної геометричної
фігури: радіус для кола, довжину та висоту для прямокутника, а також основу
та висоту для трикутника.
- Скрипт використовує ці дані для обчислення площі кожної фігури.

Функціональність:
- Запитує у користувача радіус, довжину, висоту, основу та висоту відповідних
фігур.
- Обчислює площу прямокутника, кола та трикутника за формулами.
- Виводить обчислені площі на екран.

Формули для обчислення площі:
- Площа прямокутника: довжина * ширина.
- Площа кола: π * радіус^2 (π приблизно дорівнює 3.14).
- Площа трикутника: 0.5 * основа * висота.

Використання:
- Для використання запустіть скрипт та введіть відповідні значення, коли буде
запитано.

Package version
pip - v.23.3.1

"""

print("*" * 10, "TASK 1", "*" * 10)

radius = float(input('Введіть радіус кола: '))
length = float(input('Введіть довжину прямокутника: '))
width = int(input('Введіть висоту прямокутника: '))
base = float(input('Введіть основу трикутника: '))
height = int(input('Введіть висоту трикутника: '))

r_area = length * width
c_area = 3.14 * radius * radius
t_area = .5 * base * height

if __name__ == "__main__":
    print(r_area)
    print(c_area)
    print(t_area)
