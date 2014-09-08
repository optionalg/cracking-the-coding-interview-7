

def string_compression(input_string):
    """
    implement a method to perform basic string compression using the counts of
    repeated characters. If the compressed string is not would not become
    smaller than original string, returns original string. assumes the string
    only has upper or lower case letters (a-z)
    """
    compressed_string = ''
    index = 0
    counter = 1
    while index < (len(input_string)-1):
        character = input_string[index]
        if input_string[(index + 1)] == character:
            counter += 1
            index += 1
        else:
            compressed_string += character
            compressed_string += str(counter)
            index += 1
            counter = 1
    # this is where i made the mistake
    # after loop breaks out, you need to add the final output
    compressed_string += input_string[index]
    compressed_string += str(counter)
    if len(compressed_string) < len(input_string):
        return compressed_string
    else:
        return input_string
