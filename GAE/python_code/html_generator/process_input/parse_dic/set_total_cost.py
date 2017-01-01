from tickets.get_total_cost import get_total_cost
from html_generator.process_input.parse_dic.get_list_of_prices import get_list_of_prices
from html_generator.process_input.parse_dic.get_list_of_number_of_items import get_list_of_number_of_items

def set_get_total_cost(multi_dict):

    return get_total_cost(
        get_list_of_prices(multi_dict), get_list_of_number_of_items(multi_dict))
