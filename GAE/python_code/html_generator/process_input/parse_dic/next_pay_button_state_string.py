def next_pay_button_state_string(is_clicked):
    """Only enable pay button if the previous button 
    'go_to_payment_clicked_name' has been pressed."""

    if is_clicked:
        pay_button_state = ''
    else:
        pay_button_state = 'disabled'

    return pay_button_state

def set_next_pay_button_state_string(multi_dic):

    is_clicked = multi_dic.get('go_to_payment_clicked_name')

    return next_pay_button_state_string(is_clicked)

