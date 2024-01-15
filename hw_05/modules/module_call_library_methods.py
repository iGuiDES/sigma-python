def call_library(module_name: classmethod) -> None:
    print(f"\n\n{'*' * 15} Група вимог III - Library {'*' * 15}")

    library = module_name()

    library.add_book(
        1, {
            "author": "Ерік Маттес",
            "title": "Пришвидшений курс Python",
            "publisher": "Видавництво старого лева",
            "genre": "Технічний",
            "year": 2022}
    )

    library.add_book(
        2, {
            "author": "Робер Мартін",
            "title": "Чистий код",
            "publisher": "Fabula",
            "genre": "Технчний",
            "year": 2022
        }
    )

    library.display_all_books()

    found_books = library.find_books(author = "Ерік Маттес")
    print("Знайдені книги за автором 'Ерік Маттес':", found_books)

    library.remove_book(2)
    library.display_all_books()
