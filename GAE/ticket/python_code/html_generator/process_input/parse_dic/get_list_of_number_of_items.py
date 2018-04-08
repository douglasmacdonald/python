from configuration import product_id_dic as performance_id_dic

def get_list_of_number_of_items(get_multi_dic):

    list_of_number_of_items = []
    admission_prices = performance_id_dic.get(
        get_multi_dic.get('performance_id'), {}).get('admission_price', [])
 
    for admission_price in admission_prices:
        list_of_number_of_items.append(
            get_multi_dic.get(admission_price.get('short_name')))

    return list_of_number_of_items 

def set_list_of_number_of_items(get_multi_dic):

    get_multi_dic['get_list_of_number_of_items'] = get_list_of_number_of_items

    return get_multi_dic
