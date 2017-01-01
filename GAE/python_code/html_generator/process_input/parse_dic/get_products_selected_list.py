def get_products_selected_list(admission_prices, number_of_item_dic):

    products_selected = []

    for admission_price in admission_prices:

        products_selected.append(
            {     
                'item': admission_price.get('short_name')
                , 'price_for_item' : admission_price.get('price')
                , 'number_of_item':  number_of_item_dic.get(admission_price.get('short_name'))
            }
        )

    return products_selected
