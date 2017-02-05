
# https://webapp-improved.appspot.com/guide/request.html

import process_buy_tickets_html as pr

def get_buy_tickets_no_error_handling_charge_html(
    html_template_render
    , html_page_get_multi_dic
    , logger):

    logger.info("Function: get_buy_tickets_no_error_handling_charge_html")
    html = html_template_render(
        pr.get_buy_tickets_no_error_handling_charge_html_process(
            html_page_get_multi_dic, logger))

    return html

def get_buy_tickets_html(
    html_template_render
    , html_page_get_multi_dic
    , logger):

    logger.info("Function: get_buy_tickets_html")
    html = html_template_render(
        pr.get_buy_tickets_html_process(
            html_page_get_multi_dic, logger))

    return html

def get_buy_tickets_with_error_handling_charge_html(
    html_template_render
    , html_page_get_multi_dic
    , logger):

    logger.info("Function: get_buy_tickets_with_error_handling_charge_html")
    html = html_template_render(
        pr.get_buy_tickets_charge_with_error_handling_html_process(
            html_page_get_multi_dic, logger))

    return html

def get_buy_tickets_dummy_charge_html(
    html_template_render
    , html_page_get_multi_dic
    , performance_id_dic
    , logger):

    logger.info("Function: get_buy_tickets_dummy_charge_html")
    html = html_template_render(
        pr.get_buy_tickets_dummy_charge_html_process(
            html_page_get_multi_dic, performance_id_dic, logger))

    return html
