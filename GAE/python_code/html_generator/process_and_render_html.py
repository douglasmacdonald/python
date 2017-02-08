#! /usr/bin/env python
"""Interface to the web page processing code"""

# https://webapp-improved.appspot.com/guide/request.html

# Path to local code.
import os
import sys

# HTML templates

#import local_lib.local_template_engine as te
#html_template_tickets_page_ = te.get_template('buy_tickets.html')
#html_template_index_page_ = te.get_template('index.html')


html_template_tickets_page_ = 0
html_template_index_page_ = 0

def init_template_environment(path_to_templates):
    """ e.g. path_to_templates = '../html_templates' """

    import local_lib.local_template_engine as te

    global html_template_tickets_page_
    global html_template_index_page_

    te.get_template_.init_template_environment(path_to_templates)

    html_template_tickets_page_ = te.get_template('buy_tickets.html')
    html_template_index_page_ = te.get_template('index.html')

# Logging
import logging
logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.DEBUG)

# Process and render
import process_input.process_and_render_buy_tickets_html as tt
import process_input.index_page_html as ii

def get_buy_tickets_no_error_handling_charge_html(html_page_get_multi_dic):
    logger.info("Function: get_buy_tickets_no_error_handling_charge_html")
    return tt.get_buy_tickets_no_error_handling_charge_html(
        html_template_tickets_page_.render
        , html_page_get_multi_dic
        , logger)

def get_buy_tickets_html(html_page_get_multi_dic):
    logger.info("Function: get_buy_tickets_html")
    return tt.get_buy_tickets_html(
        html_template_tickets_page_.render
        , html_page_get_multi_dic
        , logger)

def get_buy_tickets_charge_with_error_handling_html(html_page_get_multi_dic):
    logger.info("Function: get_buy_tickets_charge_with_error_handling_html")
    return tt.get_buy_tickets_with_error_handling_charge_html(
        html_template_tickets_page_.render
        , html_page_get_multi_dic
        , logger)

def get_buy_tickets_dummy_charge_html(html_page_get_multi_dic
        , performance_id_dic, sold_ticket_list):
    logger.info("Function: get_buy_tickets_dummy_charge_html")
    return tt.get_buy_tickets_dummy_charge_html(
        html_template_tickets_page_.render
        , html_page_get_multi_dic
        , performance_id_dic
        , sold_ticket_list
        , logger)

def get_index_page_html(handler_mapping, webapp_debug):
    logger.info("Function: get_index_page_html")
    return ii.get_index_page_html(
        html_template_index_page_.render
        , handler_mapping
        , webapp_debug
        , logger)
