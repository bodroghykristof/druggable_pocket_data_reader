""" This file contains general utility methods to prompt the user
to enter inputs via the CLI of the application"""


def ask_for_positive_numeric_input_with_default(text, default):
    """Asks the user to type a non-negative number by using prompt defined
    by parameter 'text'. If the user hits enter the default value will
    be returned. If the inserted number is below zero a prompt will appear
    on the console asking for correction."""

    prompt = f'{text} [{default}] : '
    while True:
        try:
            user_input = input(prompt)
            if user_input == "":
                return default
            value = int(user_input)
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a positive numeric value!")


def ask_for_binary_input_with_default(text, default):
    """Asks the user to type one of 2 options by using prompt defined
    by parameter 'text'. These two options are 'T' and 'F' standing for True
    and False correspondingly. If the user hits enter the default value will
    be returned. If the inserted value is neither 'T' nor 'F' a prompt will appear
    on the console asking for correction."""

    prompt = f'{text} [{default}] : '
    while True:
        try:
            user_input = input(prompt)
            if user_input == "":
                return default == "T"
            value = user_input.upper() == "T"
            if user_input.upper() not in ["T", "F"]:
                raise ValueError
            return value
        except ValueError:
            print(f'Input should be either T or F (or left blank for default {default}!')


def ask_not_empty_simple_input(text):
    """Asks the user to type a single non-emtpy string.
    If the inserted value is empty a prompt will appear on
    the console asking for correction."""

    prompt = f'{text} : '
    while True:
        user_input = input(prompt)
        if user_input != "":
            return user_input
        else:
            print("Input should not be empty!")
