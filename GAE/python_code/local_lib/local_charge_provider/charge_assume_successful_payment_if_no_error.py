import charge

def payment_provider_charge_(token, amount, currency, description, logger):
    """Plain charge without any other error handling"""

    logger.info("Function: payment_provider_charge_")

    return charge.charge(token, amount, currency, description, logger)

def charge_assume_successful_payment_if_no_error(
        token, amount, currency, description, logger):
    """TODO: Investigate_further_what_should_be_done_with_return.
    To check for success and what records to record.
    """

    logger.info("Function: charge_assume_successful_payment_if_no_error")

    is_payment_made = False

    try:
        charge_details = payment_provider_charge_(
            token, amount, currency, description, logger)
        is_payment_made = True

    # TODO: give a message about the internet possibly not working.
    # log and email
    # Try to keep the provider dependent details away from here,
    #except APIConnectionError as e:
    #    pass

    except Exception as e:
        logger.error(e)
        is_payment_made = False

    return is_payment_made
