from configuration import product_id_dic as performance_id_dic

def get_list_of_prices(get_multi_dic):

    list_of_prices = []
    admission_prices = performance_id_dic.get(
        get_multi_dic.get('performance_id'), {}).get('admission_price', [])

    for admission_price in admission_prices:
        list_of_prices.append(admission_price.get('price'))

    return list_of_prices
