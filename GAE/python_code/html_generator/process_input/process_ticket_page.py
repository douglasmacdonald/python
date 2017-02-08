from html_generator.process_input.parse_dic.get_currency import get_currency
from html_generator.process_input.parse_dic.get_payment_token import get_payment_token
from html_generator.process_input.parse_dic.get_performance_id import get_performance_id
from html_generator.process_input.parse_dic.get_short_description import get_short_description
from html_generator.process_input.parse_dic.get_show_id import get_show_id
from html_generator.process_input.parse_dic.is_total_cost_greater_than_zero import set_is_total_cost_greater_than_zero
from html_generator.process_input.parse_dic.next_pay_button_state_string import set_next_pay_button_state_string
from html_generator.process_input.parse_dic.set_basket_list import set_basket_list
from html_generator.process_input.parse_dic.set_default_payment_details import set_default_payment_details
from html_generator.process_input.parse_dic.set_defaults_for_missing_values import set_defaults_for_missing_values
from html_generator.process_input.parse_dic.set_list_of_products_selected_from_numbers_of_items import set_list_of_products_selected_from_numbers_of_items
from html_generator.process_input.parse_dic.set_name_on_ticket import set_name_on_ticket
from html_generator.process_input.parse_dic.set_publishable_key import set_publishable_key
from html_generator.process_input.parse_dic.set_show_information_and_title import set_show_information_and_title
from html_generator.process_input.parse_dic.set_show_information_prices import set_show_information_prices
from html_generator.process_input.parse_dic.set_show_list import set_show_list
from html_generator.process_input.parse_dic.set_show_times import set_show_times
from html_generator.process_input.parse_dic.set_ticket_list import set_ticket_list
from html_generator.process_input.parse_dic.set_total_cost import set_get_total_cost

def process(html_page_get_multi_dic, performance_id_dic, sold_ticket_list, logger):
    logger.info("Function: process")

    mutable_dict = {}

    mutable_dict['get_products_selected'] = \
        set_list_of_products_selected_from_numbers_of_items(
            html_page_get_multi_dic, performance_id_dic)

    mutable_dict['basket_list'] = set_basket_list(html_page_get_multi_dic, performance_id_dic)

    mutable_dict['description'] = get_short_description(html_page_get_multi_dic, performance_id_dic)

    mutable_dict['name_on_ticket_value'] = set_name_on_ticket(html_page_get_multi_dic)

    mutable_dict['show_id'] = get_show_id(html_page_get_multi_dic)

    mutable_dict['performance_id'] = get_performance_id(html_page_get_multi_dic)

    ( mutable_dict['payment_form_action']
    , mutable_dict['product_value']
    , mutable_dict['processed_message']) = set_defaults_for_missing_values(
        html_page_get_multi_dic)

    (mutable_dict['information_about_the_selected_show_using_show_id']
    , mutable_dict['title_for_selected_show']) = \
        set_show_information_and_title(html_page_get_multi_dic)

    mutable_dict['show_times_for_selected_show_using_show_id'] = \
        set_show_times(html_page_get_multi_dic)

    (mutable_dict['performance_information']
    , mutable_dict['performance_information_general_admission_price']
    , mutable_dict['performance_information_concession_admission_price']
    , mutable_dict['performance_information_general_admission_face_value']
    , mutable_dict['performance_information_concession_admission_face_value']) =\
        set_show_information_prices(html_page_get_multi_dic)

    mutable_dict['shows_list'] = set_show_list(html_page_get_multi_dic)

    mutable_dict.update( # update adds one dics key value pairs to another.
        set_default_payment_details(html_page_get_multi_dic))

    mutable_dict['stripe_publishable_key'] = \
        set_publishable_key(html_page_get_multi_dic)

    mutable_dict['is_input_pay_details'] = \
        set_is_total_cost_greater_than_zero(html_page_get_multi_dic)

    mutable_dict['pay_button_state'] = set_next_pay_button_state_string(
        html_page_get_multi_dic)

    mutable_dict['total_cost_value'] = set_get_total_cost(html_page_get_multi_dic)

    mutable_dict['ticket_list'] = set_ticket_list(html_page_get_multi_dic, sold_ticket_list)

    mutable_dict['token'] = get_payment_token(html_page_get_multi_dic)

    mutable_dict['currency'] = get_currency(html_page_get_multi_dic)

    return mutable_dict
