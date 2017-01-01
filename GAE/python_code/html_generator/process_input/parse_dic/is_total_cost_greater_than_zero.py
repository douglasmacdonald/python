from tickets.get_total_cost import get_total_cost
from get_list_of_prices import get_list_of_prices
from get_list_of_number_of_items import get_list_of_number_of_items

def is_input_pay_details(total_cost):

    if(total_cost > 0.0):
        is_input_pay_details = True
    else:
        is_input_pay_details = False

    return is_input_pay_details

def set_is_total_cost_greater_than_zero(multi_dict):

    return is_input_pay_details(float(get_total_cost(
        get_list_of_prices(multi_dict)
        , get_list_of_number_of_items(multi_dict))))

