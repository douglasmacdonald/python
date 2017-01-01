def reduce_on_number_of_item(products):

    new_product_list = []

    for item in products:
        n = item.get('number_of_item', 0)
        if (float(n) > 0):
            new_product_list.append(item)

    return new_product_list


