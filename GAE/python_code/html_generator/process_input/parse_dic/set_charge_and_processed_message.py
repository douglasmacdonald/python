from html_generator.process_input.parse_dic.processing_payment_provider_template_values import get_payment_provider_values_from_post_data


# Just to get the debugging going
#from python_code.tickets import sold_ticket_list

def set_charge_and_processed_message(
        charge_and_list
        , charge
        , mutable_dict
        , logger):

    logger.info("Function: set_charge_and_processed_message")

    mutable_dict['processed_message'] = charge_and_list(
        charge
        , mutable_dict
        , sold_ticket_list
        , get_payment_provider_values_from_post_data
        , logger)

    return mutable_dict
