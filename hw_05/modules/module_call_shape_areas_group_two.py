def call_shape_areas_two(
        module_name1, module_name_2, module_name_3
):
    print(f"\n\n{'*' * 15} Група вимог II - Shape Area {'*' * 15}")
    circle = module_name1(5)
    rectangle = module_name_2(10, 4)
    triangle = module_name_3(10, 5)

    print("Площа круга:", circle.calculate_area())
    print("Площа прямокутника:", rectangle.calculate_area())
    print("Площа трикутника:", triangle.calculate_area())
