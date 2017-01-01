"""Process payments using payment provider"""

import decimal
from python_code.interface import payment_provider
"""Calls the payment provider. """

#TODO: rename to payment_provider_charge

from python_code.configuration import payment_provider_api_key
from python_code.configuration import multiplier_to_minor_currency_unit

def charge_(amount, currency, token, description
    , multiplier_to_minor_currency_unit, api_key, logger):

    logger.info("Function: charge_")

    """This is to wrap in the api key."""

    payment_provider.api_key = api_key

    #TODO: possibly pass this in as a parameter. This will make it easier to
    #have a try catch just around the third party payment code.
    amount_int = int(multiplier_to_minor_currency_unit * decimal.Decimal(amount))

    charge_result = payment_provider.Charge.create(amount = amount_int
        , currency = currency, source = token, description = description)


    return charge_result

def charge(token, amount, currency, description, logger):
    """Calls charge without messy coupling.

    Not coninced by this. Having to pass an api_key and token might be specific
    to the payment method used.

    I think that I may have to even gather multi_dic processing etc togther.

    """

    logger.info("Function: charge")

    charge_result = charge_(amount, currency, token, description
        , multiplier_to_minor_currency_unit, payment_provider_api_key, logger)

    return charge_result
