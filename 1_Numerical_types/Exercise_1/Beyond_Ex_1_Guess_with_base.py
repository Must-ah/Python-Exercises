from types import UnionType
from Beyond_Ex_1_Max3Guess import print_msg,receive_and_check_input,check_user_guess_against_random_guess

def guess_random_from_list(random_list:list[int])-> int:
    from random import choice
    random_value = choice(random_list)
    assert type(random_value ) == type(1)
    return random_value

def run_one_game_with_base(random_guessed_number:int, random_base:int): #-> UnionType[str, int] :
    user_guessed = receive_and_check_input()
    user_guessed_corrected_for_base = int(str(user_guessed),random_base)
    user_guessed_to = check_user_guess_against_random_guess(user_guessed_corrected_for_base, random_guessed_number)
    user_str_guessed = f"Your guess of {user_guessed_corrected_for_base} is " + user_guessed_to
    return [user_str_guessed, user_guessed_corrected_for_base]



def guess_game_with_base() -> None:
    # ToDo implement a function that makes sure that you always get an int
    base = [2, 8, 10, 16]
    random_base = guess_random_from_list(base)

    random_int_list = list(range(0,101))

    random_str = str(guess_random_from_list(random_int_list))
    random_number = int(random_str,random_base)

    user_str_guessed, user_guessed_corrected_for_base = run_one_game_with_base(random_number,random_base)
    print_msg(user_str_guessed)

    while user_guessed_corrected_for_base != random_number:
        user_str_guessed, user_guessed_corrected_for_base = run_one_game_with_base(random_number, random_base)
        print_msg(user_str_guessed)


guess_game_with_base()
