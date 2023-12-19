"""
Виконав: Олександр Яценко
Homework 1 - II рівень складності

Цей скрипт виконує формування та вивід особистої інформації для CV.

Особливості:
- Виводить навчальні дані, навички та загальну інформацію про особу.
- Навчальні дані, навички та загальна інформація задаються у вигляді списків
та словників.

Структура даних:
- education: список, що містить інформацію про освіту.
- skills: кортеж, який містить перелік навичок.
- cv_personal_info: словник, що містить загальну інформацію про особу (ім'я
та електронну пошту).

Функціональність:
- Формує рядки з інформацією про освіту, навички та загальні дані.
- Виводить сформовану інформацію на екран.

Використання:
- Запустіть скрипт для виведення інформації про освіту, навички та особисті
дані.

Package version:
pip v.23.3.1
"""

print("*" * 10, "TASK 2", "*" * 10)

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

out_education = education[0]

out1_skills = f' - 1 {skills[0]}'
out2_skills = f' - 2 {skills[1]}'
out3_skills = f' - 3 {skills[2]}'

out1_general_info = f'- Імʼя:, {cv_personal_info['name']}'
out2_general_info = f'- Email:, {cv_personal_info['email']}'

if __name__ == "__main__":
    print('\nEducation:')
    print(out_education)
    print('\nSkills:')
    print(out1_skills, out2_skills, out3_skills, sep = "\n")
    print('\nGeneral Information')
    print(out1_general_info, out2_general_info, sep = "\n")
