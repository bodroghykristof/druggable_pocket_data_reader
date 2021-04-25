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
