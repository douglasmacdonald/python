from basket_list_create import basket_list_create
from reduce_on_number_of_item import reduce_on_number_of_item
from cost_of_items_list import cost_of_items_list
from replace_nones_with_zeros import replace_nones_with_zeros
from html_generator.process_input.parse_dic.set_list_of_products_selected_from_numbers_of_items import set_list_of_products_selected_from_numbers_of_items

def set_basket_list(multi_dict):

    products_selected = set_list_of_products_selected_from_numbers_of_items(multi_dict)
    products_selected = replace_nones_with_zeros(products_selected)
    products_selected = reduce_on_number_of_item(products_selected)

    costs_list = cost_of_items_list(products_selected)

    basket_list = basket_list_create(products_selected, costs_list
        , multi_dict.get('name_on_ticket_name', ""))

    return basket_list
