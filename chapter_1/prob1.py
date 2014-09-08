# implement an algo to determine if a string has all unique characters


def all_unique(input_string):
    if len(set(input_string)) != len(input_string):
        return False
    else:
        return True
    # better version
    # return len(set(input_string)) == len(input_string)


def all_unique_without_data(input_string):
    if len(input_string) == 1:
        return True
    else:
        character = input_string[0]
        for x in input_string[1:]:
            if character == x:
                return False
        return all_unique_without_data(input_string[1:])

    # better version
    # for i in input_string:
        # if input_string.count(i) > 1:
            # return False
    # else:
        # return True
