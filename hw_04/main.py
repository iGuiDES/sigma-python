# CV module
from modules.cv import create_txt_content as ctc
from modules.cv import create_cv_file as ccf
from modules.cv import create_md_content as cmc
# Area figure module
from modules.area_figures import calculate_circle_area as cca
from modules.area_figures import calculate_rectangle_area as cra
# FizzBuzz
from modules.fizzbuzz import fizz_buzz_game as fbg

# For create CV
education = [
    "Вчитель фізичного виховання та спорту, Сарненський педагогічний коледж"
]

skills = (
    "Python",
    "Linux",
    "Docker"
)

cv_personal_info = {
    "name": "Яценко Олександр",
    "email": "iosiguides@gmail.com"
}

if __name__ == "__main__":
    # CV create
    print(f'{"*" * 15} CV {"*" * 15}')
    cv_format = input(
        'Виберіть формат CV (text, md): '
    )

    if cv_format == 'md':
        md_content = cmc(cv_personal_info, education, skills)
        ccf("cv.md", md_content)
    elif cv_format == 'text':
        txt_content = ctc(cv_personal_info, education, skills)
        ccf("cv.txt", txt_content)

    # Area Figures
    print(f'\n\n{"*" * 15} Area Figures {"*" * 15}')
    user_answer = input(
        'Виберіть та введіть одне із значень в дужках ("circle", "rectangle"): '
    )

    if user_answer.lower() == 'circle':
        circle_radius: int = int(input('Введіть радіус кола: '))
        print(cca(circle_radius))

    elif user_answer.lower() == 'rectangle':
        length: float = int(input('Введіть довжину прямокутника: '))
        width: float = float(input('Введіть висоту прямокутника: '))
        print(cra(length, width))

    # FizzBuzz
    print(f'\n\n{"*" * 15} Fizz Buzz Game {"*" * 15}')
    start = int(input('Введіть стартове число: '))
    end = int(input('Введіть кінцеве число: '))
    result = fbg(start, end)
    print(f'Результат: {result}')
