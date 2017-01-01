from itertools import izip

def basket_list_create(products, costs_list, name_on_ticket):

    basket_list = []
    for item, sub_total_cost in izip(products, costs_list):

        n = item['number_of_item'];

        d = { 'number_of_item':item['number_of_item']
                , 'item_description':item['item']
                , 'your_description':name_on_ticket
                , 'price':item['price_for_item']
                , 'cost':sub_total_cost}

        basket_list.append(d)

    return basket_list



