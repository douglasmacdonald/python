from tickets.price_for_tickets import multiply as multiply

def cost_of_items_list(products):

    costs = []
    for item in products:
        n = item['number_of_item'];
        if n:
            costs.append(multiply(n, item['price_for_item']))
        else: 
            costs.append("0.00")

    return costs
