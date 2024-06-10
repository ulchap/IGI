def count_digits_and_letters(input_string):
    digit_count = 0
    letter_count = 0

    for char in input_string:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            letter_count += 1

    return digit_count, letter_count