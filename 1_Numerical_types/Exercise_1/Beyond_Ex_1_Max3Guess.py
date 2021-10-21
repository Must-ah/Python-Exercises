# I will chop up the code into segments to be reused later.


def receive_and_check_input(msg:str = "Guess a number between 0 and 100 -> ")-> int:
    user_guess_str = input((msg))
    assert user_guess_str.isdigit() == True
    user_guessed_int = int(user_guess_str)
    return user_guessed_int

def print_msg(msg:str) -> None:
    print(msg)


def check_user_guess_against_random_guess(user_guess:int, random_guess:int) -> str:
    if user_guess > random_guess:
        return "too high!"
    elif user_guess < random_guess:
         return "too low!"
    else:
        return "Correct!"

def run_one_game(random_guessed_value:int, msg:str = "Guess a number between 0 and 100 -> ")-> int:
    user_guessed = receive_and_check_input(msg)
    user_guessed_to = check_user_guess_against_random_guess(user_guessed, random_guessed_value)
    message_str = f"Your guess of {user_guessed} is "+user_guessed_to
    print_msg(message_str)
    return user_guessed
    

def guessing_game_3_attempts()-> None:
    from random import randint
    my_guessing_value = randint(0,100)
    user_guessed = -10
    game_counter = 0
    game_status_msg = "Congratulation you guessed correct!"
    while user_guessed != my_guessing_value:
        if game_counter  > 2:
            game_status_msg = "Sorry you guessed wrong 3 times!"
            break
        user_guessed = run_one_game(my_guessing_value, "Guess a number between 0 and 100 -> ")
        game_counter+=1

    print_msg(game_status_msg)

# guessing_game_3_attempts()
    

    
