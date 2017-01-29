
from python_code.configuration import product_id_dic as performance_id_dic
#from configuration import product_id_dic as performance_id_dic

#from python_code.configuration import product_id_dic as performance_id_dic

from get_number_for_item import get_number_for_item
from get_products_selected_list import get_products_selected_list

def set_list_of_products_selected_from_numbers_of_items(multi_dict
    , performance_id_dic):

    admission_prices = performance_id_dic.get(
        multi_dict.get('performance_id'), {}).get('admission_price', [])

    number_for_item_dic = get_number_for_item(admission_prices, multi_dict)

    products_selected = get_products_selected_list(admission_prices
        , number_for_item_dic)

    return products_selected
