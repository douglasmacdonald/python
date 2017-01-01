def get_number_for_item(admission_prices, multi_dict):

    number_of_item_dic = {}
    for admission_price in admission_prices:
        key = admission_price.get('short_name')
        number_of_item_dic[key] = multi_dict.get(key, 0)

    return number_of_item_dic
