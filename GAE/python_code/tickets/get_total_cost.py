from itertools import izip
from tickets.price_for_tickets import add as add
from tickets.price_for_tickets import multiply as multiply

def get_total_cost(list_of_prices, list_number_of_each):

    total_cost = "0.00"

    for n, p in izip(list_number_of_each, list_of_prices):

        if n:
            total_cost = add(total_cost, multiply(n, p))
        
    return total_cost
