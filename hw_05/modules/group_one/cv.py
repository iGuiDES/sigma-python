"""
    Виконавець: Олександр Яценко
    Homework V - Група вимог I

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


class CVCreator:
    def __init__(self, personal_info: dict, edu: list, p_skills: tuple) -> None:
        self.personal_info = personal_info
        self.edu = edu
        self.p_skills = p_skills

    def create_txt_content(self):
        content = (f"Ім'я: {self.personal_info['name']}\nEmail: "
                   f"{self.personal_info['email']}\n\nОсвіта:\n")
        for education in self.edu:
            content += f"- {education}\n"

        content += "\nНавички:\n"
        for skill in self.p_skills:
            content += f"- {skill}\n"
        return content

    def create_md_content(self):
        content = (f"# {self.personal_info['name']}\n\n**Email**: "
                   f"{self.personal_info['email']}\n\n## Освіта\n")
        for education in self.edu:
            content += f"- {education}\n"

        content += "\n## Навички\n"
        for skill in self.p_skills:
            content += f"- {skill}\n"
        return content

    @staticmethod
    def create_cv_file(file_name, content):
        try:
            with open(file_name, 'w', encoding = 'utf-8') as file:
                file.write(content)
        except Exception as e:
            print(f"Помилка створення файлу {file_name}: {e}")
        else:
            print(f"{file_name} файл було успішно створено")
        finally:
            print(
                f"Ознайомитися з результатом можна: "
                f"{os.path.abspath(file_name)}"
                )
