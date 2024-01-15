def call_fizzbuzz(module_name):
    print(f"\n\n{'*' * 15} Група вимог I - FizzBuzz {'*' * 15}")
    game_one = module_name(1, 15)
    game_two = module_name(10, 45)
    result_one = game_one.play_game()
    result_two = game_two.play_game()
    print(result_one, result_two, sep = '\n')
