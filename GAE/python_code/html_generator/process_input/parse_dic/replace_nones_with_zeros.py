def replace_nones_with_zeros(products):

    new_product_list = []

    for item in products:     
        if (item.get('number_of_item', 0) == None):
            item['number_of_item'] = 0

        new_product_list.append(item)

    return new_product_list
