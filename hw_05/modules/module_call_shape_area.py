def call_shape_area(module_name):

    print(f"\n\n{'*' * 15} Група вимог I - Area {'*' * 15}")
    calculator = module_name()
    circle_area = calculator.calculate_circle_area(10)
    rectangle_area = calculator.calculate_rectangle_area(5, 4)

    print(f"Площа круга: {circle_area}")
    print(f"Площа прямокутника: {rectangle_area}")
