"""
    Виконавець: Олександр Яценко
    Homework V - Група вимог IІ

    Цей скрипт створює два файли резюме (CV) у форматах .txt і .md

    Package name _____________________ version
    pip          _____________________ v23.3.1
"""

import os


class CVCreator:
    def __init__(self, personal_info):
        self.personal_info = personal_info

    def create_txt_content(self):
        raise NotImplementedError

    def create_md_content(self):
        raise NotImplementedError

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


class PersonCV(CVCreator):
    def __init__(self, person_info, education, person_skills):
        super().__init__(person_info)
        self.edu = education
        self.skills = person_skills

    def create_txt_content(self):
        content = (f"Ім'я: {self.personal_info['name']}\nEmail: "
                   f"{self.personal_info['email']}\n\nОсвіта:\n")
        for education in self.edu:
            content += f"- {education}\n"
        content += "\nНавички:\n"
        for skill in self.skills:
            content += f"- {skill}\n"
        return content

    def create_md_content(self):
        content = (f"# {self.personal_info['name']}\n\n"
                   f"**Email**: {self.personal_info['email']}\n\n## Освіта\n")
        for education in self.edu:
            content += f"- {education}\n"
        content += "\n## Навички\n"
        for skill in self.skills:
            content += f"- {skill}\n"
        return content
