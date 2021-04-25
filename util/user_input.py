def ask_for_positive_numeric_input_with_default(text, default):
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
    prompt = f'{text} : '
    while True:
        user_input = input(prompt)
        if user_input != "":
            return user_input
        else:
            print("Input should not be empty!")
