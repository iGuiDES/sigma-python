"""
    Виконав: Олександр Яценко
    Homework III - Група вимог I-II

    Цей скрипт створює два файли резюме (CV) для особи з вказаною освітою,
    навичками та особистою інформацією.
    Файли створюються у форматах .txt і .md (Markdown). Для формування змісту
    файлів використовуються
    цикли та умовні оператори. Також застосовується обробка винятків для
    управління помилками при створенні файлів.

    Дані для CV вводяться вручну в скрипті. Скрипт виконується без визначення
    власних функцій (за винятком однієї
    допоміжної функції), але може використовувати сторонні бібліотеки.

    Package name _____________________ version
    pip          _____________________ v23.3.1
    os           _____________________ v3.12.1
"""

import os

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


def create_cv_file(file_name, content):
    """
        Створює файл резюме з вказаним ім'ям файлу та вмістом.

        Параметри:
        file_name (str): Назва файлу, який буде створено.
        content (str): Вміст файлу, який буде записаний у файл.

        Ця функція відкриває (або створює, якщо такого файлу не існує) файл з
        вказаним ім'ям
        та записує в нього вміст. У разі помилок при роботі з файлом,
        вони обробляються за допомогою
        блоку try-except. Після завершення роботи функція виводить повідомлення
        про успіх або помилку.

        Returns:
        None
    """

    try:
        with open(file_name, 'w', encoding = 'utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"Помилка створення файлу {file_name}: {e}")
    else:
        print(f"{file_name} файл було успішно створено")
    finally:
        print(f"Ознайомитися з результатом можна: {os.path.abspath(file_name)}")


if __name__ == '__main__':
    txt_content = (f"Ім'я: {cv_personal_info['name']}\nEmail: "
                   f"{cv_personal_info['email']}\n\nОсвіта:\n")
    for edu in education:
        txt_content += f"- {edu}\n"

    txt_content += "\nНавички:\n"
    for skill in skills:
        txt_content += f"- {skill}\n"

    md_content = f"# {cv_personal_info['name']}\n\n**Email**: {cv_personal_info[
        'email']}\n\n## Освіта\n"
    for edu in education:
        md_content += f"- {edu}\n"

    md_content += "\n## Навички\n"
    for skill in skills:
        md_content += f"- {skill}\n"

    create_cv_file("cv.txt", txt_content)
    create_cv_file("cv.md", md_content)
