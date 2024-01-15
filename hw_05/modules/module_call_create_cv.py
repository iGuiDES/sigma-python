def call_cv_create(module_name: classmethod) -> None:
    print(f"\n\n{'*' * 15} Група вимог I - CV {'*' * 15}")
    personal_info = {
        "name": "Олександр Яценко",
        "email":"iosiguides@gmail.com"
    }
    education = [
        "Сарненський педагогічний коледж",
        "Sigma"
    ]
    skills = (
        "Python",
        "HTML",
        "CSS",
        "JavaScript"
    )

    cv_creator = module_name(personal_info, education, skills)
    txt_content = cv_creator.create_txt_content()
    md_content = cv_creator.create_md_content()

    cv_creator.create_cv_file("resume.txt", txt_content)
    cv_creator.create_cv_file("resume.md", md_content)
