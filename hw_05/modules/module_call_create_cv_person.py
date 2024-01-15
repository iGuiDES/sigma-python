def call_create_cv_person(module_name: classmethod) -> None:
    print(f"\n\n{'*' * 15} Група вимог II - CV for All {'*' * 15}")
    person_info = {'name': 'Яценко Олександр', 'email': 'iosiguides@gmail.com'}
    education = ['Сарненський педагогічний коледж', 'Sigma']
    person_skills = ('Python', 'Data Analysis')

    person_cv = module_name(person_info, education, person_skills)
    print(person_cv.create_txt_content())
