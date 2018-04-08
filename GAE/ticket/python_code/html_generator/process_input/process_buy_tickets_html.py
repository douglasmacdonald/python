################################################################################
# Process html in
################################################################################

from process_ticket_page import process as process_ticket
from process_charge_page import charge_add_to_ticket_list_no_error_handling
from process_charge_page import charge_add_to_ticket_list_with_error_handling
from process_charge_page import no_charge_and_add_to_ticket_list

# TODO: should the process ticket page be called again. Might this make it
# more likely that the ticket list will be updated correctly.

def get_buy_tickets_no_error_handling_charge_html_process(
    html_page_get_multi_dic, logger):

    logger.info("Function: get_buy_tickets_no_error_handling_charge_html_process")

    mutable_dict = process_ticket(html_page_get_multi_dic, logger)

    template_variables = charge_add_to_ticket_list_no_error_handling(
        mutable_dict, logger)

    return template_variables

def get_buy_tickets_html_process(html_page_get_multi_dic, logger):

    logger.info("Function: get_buy_tickets_html_process")

    template_variables = process_ticket(html_page_get_multi_dic, logger)

    return template_variables

def get_buy_tickets_charge_with_error_handling_html_process(
    html_page_get_multi_dic, logger):

    logger.info(
    "Function: get_buy_tickets_charge_with_error_handling_html_process")

    mutable_dict = process_ticket(html_page_get_multi_dic, logger)

    template_variables = charge_add_to_ticket_list_with_error_handling(
        mutable_dict, logger)

    return template_variables

def get_buy_tickets_dummy_charge_html_process(html_page_get_multi_dic, logger):

    logger.info("Function: get_buy_tickets_dummy_charge_html_process")

    mutable_dict = process_ticket(html_page_get_multi_dic, logger)

    template_variables = no_charge_and_add_to_ticket_list(mutable_dict, logger)

    return template_variables
