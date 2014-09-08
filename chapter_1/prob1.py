# implement an algo to determine if a string has all unique characters


def all_unique(input_string):
    if len(set(input_string)) != len(input_string):
        return False
    else:
        return True


def all_unique_without_data(input_string):
    pass