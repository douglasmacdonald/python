import sys

from tickets.get_total_cost import get_total_cost
from get_list_of_prices import get_list_of_prices
from get_list_of_number_of_items import get_list_of_number_of_items

def charge_and_add_to_ticket_list(charge, get_multi_dic, ticket_list
    , get_payment_provider_values_from_post_data, logger):

    logger.info("Function: charge_and_add_to_ticket_list")

    token, amount, currency, description = \
        get_payment_provider_values_from_post_data(get_multi_dic)


    is_payment_made = False
    try:
        #TODO: Check what error catching needs to be done.
        #TODO: Split up and bubble up some of the contained logic in charge.
        is_payment_made = charge(token, amount, currency, description, logger)

    except Exception as e:
        #TODO: probably need to double check that payment was not made as my
        #code could have bombed out after the payment was made. Hmmm, I was
        #moving this try/except to higher levels to expose the logic but I am
        #now thinking that I probably want it tightly around the third party
        #call. The best of both worlds would come from passing it in. I.e. pass
        #into the function the call which would have the same interface with or
        #without the try/catch.

        logger.error(e)

        is_payment_made = False

    if is_payment_made:
        append_to_ticket_list(get_multi_dic, ticket_list
            , get_payment_provider_values_from_post_data)

    return is_payment_made

def no_charge_and_add_to_ticket_list(charge, get_multi_dic, ticket_list
    , get_payment_provider_values_from_post_data):
    """The charge parameter is simply not used."""

    is_payment_made = False

    append_to_ticket_list(get_multi_dic, ticket_list
        , get_payment_provider_values_from_post_data)

    return is_payment_made


def append_to_ticket_list(get_multi_dic, ticket_list
    , get_payment_provider_values_from_post_data):

    key = ticket_list.append(ticket_number = ""
        , name_on_ticket = get_multi_dic.get('name_on_ticket_name', "")
        , total_cost = get_total_cost(get_list_of_prices(get_multi_dic)
        , get_list_of_number_of_items(get_multi_dic)))


    # Try to force a database write. Try ignoring the cache.
    key.get()
