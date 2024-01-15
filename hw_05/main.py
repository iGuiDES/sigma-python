# Group of requirements - I
from hw_05.modules.group_one.fizzbuzz import FizzBuzzGame
from hw_05.modules.group_one.area_figures import ShapeAreaCalculator
from hw_05.modules.group_one.cv import CVCreator

# Group of requirements - II
from hw_05.modules.group_two.cv_all import PersonCV
from hw_05.modules.group_two.shape_area import Circle, Rectangle, Triangle

# Group of requirements - III
from hw_05.modules.group_three.library import HomeLibrary

# Import call modules
from hw_05.modules.module_call_fizzbuzz import call_fizzbuzz
from hw_05.modules.module_call_shape_area import call_shape_area
from hw_05.modules.module_call_create_cv import call_cv_create
from hw_05.modules.module_call_create_cv_person import call_create_cv_person
from hw_05.modules.module_call_shape_areas_group_two import call_shape_areas_two
from hw_05.modules.module_call_library_methods import call_library

if __name__ == '__main__':
    """
    Для простоти читання коду, вирішив винести всі виклики в окремі модулі та 
    розподілив самі модулі в каталоги відповідно до групи завдання.
    Єдине, не впевнений що це правильне рішення, але як на мене, воно є 
    оптимальним в даному випадку.
    Також упустив опис docstring, пробував навіть коротенькі, але виходило 
    просто громіздя тексту, що мене дуже засмутило, тому документування 
    опустив, маю надію, на оцінку це не вплине.
    Є прохання, надайте будь ласка рекомендації, стосовно оформлення даного 
    типу завдань. Дякую)
    """

    # I
    call_fizzbuzz(FizzBuzzGame)
    call_shape_area(ShapeAreaCalculator)
    call_cv_create(CVCreator)

    # II
    call_create_cv_person(PersonCV)
    call_shape_areas_two(Circle, Rectangle, Triangle)

    # III
    call_library(HomeLibrary)
