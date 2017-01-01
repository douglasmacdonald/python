def get_payment_token(html_page_get_multi_dic):

    return html_page_get_multi_dic.get('stripeToken', '')
