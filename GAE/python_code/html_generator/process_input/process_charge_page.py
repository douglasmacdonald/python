from html_generator.process_input.parse_dic.set_charge_and_processed_message import set_charge_and_processed_message
from html_generator.process_input.parse_dic.charge_and_add_to_ticket_list import charge_and_add_to_ticket_list
from html_generator.process_input.parse_dic.charge_and_add_to_ticket_list import no_charge_and_add_to_ticket_list_2

#from python_code.local_lib.local_charge_provider.charge_assume_successful_payment_if_no_error import charge_assume_successful_payment_if_no_error as charge_debug
#from python_code.local_lib.local_charge_provider.charge import charge

def charge_ticket_list_(charge_and_list
    , charge_function
    , mutable_dict
    , sold_ticket_list
    , logger):

    #raise ImportError("Just to get the debugging going, commented out import")

    logger.info("Function: charge_ticket_list_")

    mutable_dict = set_charge_and_processed_message(
        charge_and_list
        , charge_function
        , mutable_dict
        , sold_ticket_list
        , logger)

    return mutable_dict

def charge_add_to_ticket_list_no_error_handling(html_page_get_multi_dic, logger):
    """Basic charge without error handling."""

    logger.info("Function: charge_add_to_ticket_list_no_error_handling")

    mutable_dict = charge_ticket_list_(
        charge_and_add_to_ticket_list
        , charge
        , html_page_get_multi_dic
        , sold_ticket_list
        , logger)

    return mutable_dict

def charge_add_to_ticket_list_with_error_handling(html_page_get_multi_dic, logger):
    """Charge with error handling.

    Deployment code."""

    #TODO: Possibly make the error handling more precise for the charge.

    logger.info("Function: charge_add_to_ticket_list_with_error_handling")

    mutable_dict = charge_ticket_list_(
         charge_and_add_to_ticket_list
        , charge_debug
        , html_page_get_multi_dic
        , sold_ticket_list
        , logger)

    return mutable_dict

def no_charge_and_add_to_ticket_list(
    html_page_get_multi_dic
    , charge_debug
    , sold_ticket_list
    , logger):
    """Charge mocked.

    For development when offline but the charge is mocked. The charge
    parameter is simply not used."""

    logger.info("Function: no_charge_and_add_to_ticket_list")

    mutable_dict = charge_ticket_list_(
        no_charge_and_add_to_ticket_list_2
        , charge_debug
        , html_page_get_multi_dic
        , sold_ticket_list
        , logger)

    return mutable_dict
