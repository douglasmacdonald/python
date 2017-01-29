#import python_code.tickets.charge.charge as charge

#import python_code.local_lib.local_charge_provider.charge as charge

def get_payment_provider_values_from_post_data(post_data_multi_dic, charge):
    """ Strip the relevant post data from the pay page.

    The data stripped from post is dependant on the pay page.
    'stripeToken' added to post by Stripe.

    The conversion for amount is dependant on 'Stripe'.

    The return values are needed for the Stripe stripe.Charge.create
    """

    token = post_data_multi_dic.get('token', '')
    amount = post_data_multi_dic.get('total_cost_value', '')
    currency = post_data_multi_dic.get('currency', '')
    #description = post_data_dic['description']
    #description = post_data_multi_dic.get('description', '???')
    description = "TODO: processing_payment_provider_template_values.py"

    return token, amount, currency, description
