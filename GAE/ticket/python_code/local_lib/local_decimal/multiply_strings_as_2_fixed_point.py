import decimal

def multiply_strings_as_2_fixed_point(str_1, str_2):
    D = decimal.Decimal
    price_decimal = (D(str_1) * D(str_2)).quantize(D('0.01'))
    cost_str = str(price_decimal)
    return cost_str

def add_strings_as_2_fixed_point(str_1, str_2):
    D = decimal.Decimal
    price_decimal = (D(str_1) + D(str_2)).quantize(D('0.01'))
    cost_str = str(price_decimal)
    return cost_str
