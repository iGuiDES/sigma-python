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



