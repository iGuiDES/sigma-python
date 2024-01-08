"""
Виконавець: Олександр Яценко
Homework III - Група вимог I-II

Цей скрипт створює два файли резюме (CV) у форматах .txt і .md для особи з
вказаною освітою,
навичками та особистою інформацією. Файли формуються за допомогою функцій,
що враховують
форматування відповідних типів файлів. Скрипт використовує модуль os для
визначення шляху до файлів
та обробки винятків при створенні файлів.

Package name _____________________ version
pip          _____________________ v23.3.1
os           _____________________ v3.12.1
"""
import os


def create_txt_content(personal_info, edu, p_skills):
    """
    Створює зміст резюме у форматі .txt.

    Параметри:
    personal_info (dict): Словник з особистою інформацією.
    education (list): Список освітніх закладів.
    skills (tuple): Кортеж навичок.

    Returns:
    str: Створений зміст у форматі .txt.
    """
    content = (f"Ім'я: {personal_info['name']}\nEmail: "
               f"{personal_info['email']}\n\nОсвіта:\n")
    for edu in edu:
        content += f"- {edu}\n"

    content += "\nНавички:\n"
    for skill in p_skills:
        content += f"- {skill}\n"
    return content


def create_md_content(personal_info, edu, p_skills):
    """
    Створює зміст резюме у форматі Markdown (.md).

    Параметри:
    personal_info (dict): Словник з особистою інформацією.
    education (list): Список освітніх закладів.
    skills (tuple): Кортеж навичок.

    Returns:
    str: Створений зміст у форматі Markdown.
    """
    content = f"# {personal_info['name']}\n\n**Email**: {personal_info[
        'email']}\n\n## Освіта\n"
    for edu in edu:
        content += f"- {edu}\n"

    content += "\n## Навички\n"
    for skill in p_skills:
        content += f"- {skill}\n"
    return content


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
