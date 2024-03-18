"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Anetta Martináková
email: martinakova.anetta@gmail.com
discord: Anetta M.#5044 (or originally known as zrzavahlava#5044)
"""

import string
import random
import time

print("Hi there\n"
      f"{47 * '-'}\n"
      "I've generated a random 4 digit number for you.\n"
      "Let's play a bulls and cows game.\n"
      f"{47 * '-'}")


def generate_secret_number() -> str:
    """
    Generating random 4 digits number without duplicates, cannot start with 0

    :return:
        str: 4 digits number as a string
    :example:
    >>> secret_number = generate_secret_number()
    >>> len(secret_number) == 4
    True
    >>> secret_number.isdigit()
    True
    >>> secret_number.startswith('0')
    False
    """
    while True:
        secret_number = ''.join(random.sample(string.digits, 4))
        if not secret_number.startswith('0'):
            return secret_number


def validate_user_guess(secret_number: str, number_from_user: str) -> str:
    """
    Validate if user inputs unique 4 digits number without duplicates, number cannoct start with 0,
    cannot contain non-numeric characters.

    :args:
        secret_number (str): the secret number to be guessed by the user
        number_from_user (str): user's guess
    :return:
        str: feedback for the user's guess
             returns "Incorrect number" if the user's input is invalid
    :example:
    >>> validate_user_guess('1234', '5678')
    '0 bulls, 0 cows'
    >>> validate_user_guess('1234', '1223')ß
    'Please use unique numbers only.'
    >>> validate_user_guess('1234', '122x')
    'Please use digits only.'
    >>> validate_user_guess('1234', '123')
    'Your number must have 4 digits!'
    >>> validate_user_guess('1234', '0123')
    'Number cannot start with zero!'
    """
    if number_from_user.startswith('0'):
        return "Number cannot start with zero!"
    if len(number_from_user) != 4:
        return "Your number must have 4 digits!"
    if not number_from_user.isdigit():
        return "Please use digits only."
    if len(set(number_from_user)) != 4:
        return "Please use unique numbers only."
    bulls = sum(1 for i in range(4) if secret_number[i] == number_from_user[i])
    cows = len(set(secret_number).intersection(number_from_user)) - bulls
    return f"{bulls} bull{'' if bulls == 1 else 's'}, {cows} cow{'' if cows == 1 else 's'}"


secret_number = generate_secret_number()
start_time = time.time()
attempts = 0

while True:
    number_from_user = input("Enter a number:\n"
                             f"{'-' * 47}\n")
    attempts += 1
    result = validate_user_guess(secret_number, number_from_user)
    print(result)
    if "4 bulls" in result:
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Congratulations! You guessed the secret number. You guessed the secret number in {attempts} attempts."
              f" It took you {time_taken:.2f} seconds.")
        break

if __name__ == "__main__":
    import doctest
    doctest.testmod()







