
def guessing_game()-> None:
    from random import randint
    my_guessing_value = randint(0,100)
    user_guessed = -10

    while user_guessed != my_guessing_value:
        user_guess_str = input(("Guess a number between 0 and 100 -> "))
        assert user_guess_str.isdigit() == True
        user_guessed = int(user_guess_str)
        message_str = f"Your guess of {user_guessed} is too "
        if user_guessed > my_guessing_value:
            print(message_str+"high!")
        else:
            print(message_str+"low!")

    
    print(f"Congratulation you guessed correct!")

guessing_game()

    




