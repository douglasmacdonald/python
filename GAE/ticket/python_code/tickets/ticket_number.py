# The next line is probably broken
# Look in local library for the import
from interface import check_digit_algorithm

def encode(number):
    return check_digit_algorithm.encode(number)

def generate_ticket_number():

    next_number = get_next_number()

    check_digit = encode(next_number)

    number_with_check_digit = str(next_number) + str(check_digit)

    return number_with_check_digit
