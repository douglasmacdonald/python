from local_lib.local_decimal.multiply_strings_as_2_fixed_point import multiply_strings_as_2_fixed_point
from local_lib.local_decimal.multiply_strings_as_2_fixed_point import add_strings_as_2_fixed_point

def multiply(number, price):
    
    cost = multiply_strings_as_2_fixed_point(price, number)

    return cost

def add(val1, val2):

    cost = add_strings_as_2_fixed_point(val1, val2)

    return cost
    
