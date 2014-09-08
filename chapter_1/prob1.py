# implement an algo to determine if a string has all unique characters


def all_unique(input_string):
    if len(set(input_string)) > 26:
        return False
    else:
        return True