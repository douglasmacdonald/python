"Interface to the handlers, mapping and webapp run."

import sys
import os

# Path to local code.
additional_path = os.path.join(sys.path[0], "python_code")
if additional_path not in sys.path: sys.path.append(additional_path)

from local_lib import webapp

#from html_generator import index_page_html
#from html_generator import process_and_render_buy_tickets_html

from html_generator import process_and_render_html
path_to_templates = 'html_templates'
process_and_render_html.init_template_environment(path_to_templates)

################################################################################
# Functions that return a webapp.
#
# These are selected via the start up yaml file.
#
# Attempting to accumulate the path logic in one place.
################################################################################

def run_main_charge_with_no_error_handling():

    return run_webframework_(
        page_to_charge_with_no_error_handling_list(
               create_page_to_handler_mapping_common_list())
            , webapp_debug_flag = True)

def run_dummy_charge_debug():
    """Return webapp with a dummy payment provider.

    The dummy payment provider is useful when developing and there is no
    internet connection. It indicates a sucessful payment.
    """

    return run_webframework_(
        create_page_to_dummy_payment(
            create_page_to_handler_mapping_common_list())
        , webapp_debug_flag = True)

def run_debug():
    """Return webapp with the debug set to true."""

    return run_webframework_(
        create_page_to_handler_mapping_list(
            create_page_to_handler_mapping_common_list())
        , webapp_debug_flag = True)

def run():
    """Return the production webapp."""
    return run_webframework_(
        create_page_to_handler_mapping_list(
            create_page_to_handler_mapping_common_list())
        , webapp_debug_flag = False)

def run_webframework_(handler_mapping, webapp_debug_flag):
    """Groups code for kicking off the webframwork."""

    config = {'handler_mapping': handler_mapping}

    return webapp.WSGIApplication(handler_mapping, config = config
        , debug = webapp_debug_flag)

################################################################################
# Handlers
################################################################################
class BuyTickets(webapp.RequestHandler):
    """This is all the ticket purchase excluding the charge handling."""
    def get(self):
        return self.get_and_post_()

    def post(self):
        return self.get_and_post_()

    def get_and_post_(self):

        html = process_and_render_html.get_buy_tickets_html(self.request.params)

        return webapp.Response(html)

class ChargeWithErrorHandling(webapp.RequestHandler):
    """This is the production code. This is the ticket purchase in of the
    BuyTickets followed by the charge handling."""

    def get(self):
        return self.get_and_post_()

    def post(self):
        return self.get_and_post_()

    def get_and_post_(self):
        html = process_and_render_html.get_buy_tickets_charge_with_error_handling_html(self.request.params)

        return webapp.Response(html)

class ChargeNoErrorHandling(webapp.RequestHandler):
    """For development or debugging. This charge does not handle errors in the
    call to the charge."""

    def get(self):
        return self.get_and_post_()

    def post(self):
        return self.get_and_post_()

    def get_and_post_(self):
        html = process_and_render_html.get_buy_tickets_no_error_handling_charge_html(
            self.request.params)

        return webapp.Response(html)


class DummyCharge(webapp.RequestHandler):
    """For development when offline but the charge is mocked. In fact, the
    charge is ignored, the ticket list appended and false (charge) returned. So
    there is no point in passing in other 'charge' (debug or non-debug)
    functions."""

    def get(self):
        return self.get_and_post_()

    def post(self):
        return self.get_and_post_()

    def get_and_post_(self):
        html = process_and_render_html.get_buy_tickets_dummy_charge_html(
            self.request.params)

        return webapp.Response(html)

class Index(webapp.RequestHandler):
    "Create and writes the 'index.html' page."

    def get(self):
        handler_mapping = self.app.config.get('handler_mapping')

        html = process_and_render_html.get_index_page_html(
            handler_mapping = handler_mapping
            , webapp_debug = self.app.debug)

        return webapp.Response(html)

################################################################################
# Mapping between page and handler
################################################################################
def create_page_to_handler_mapping_common_list():
    return [('/', Index)
            , ('/buy_tickets' , BuyTickets)
            , ('/buy_tickets/' , BuyTickets)]

def page_to_charge_with_no_error_handling_list(handler_mapping):
    """For development or debugging. This charge does not handle errors in the
    call to the charge."""
    handler_mapping.append(('/buy_tickets/charge', ChargeNoErrorHandling))
    handler_mapping.append(('/buy_tickets/charge/', ChargeNoErrorHandling))
    return handler_mapping

def create_page_to_handler_mapping_list(handler_mapping):
    """This is the most appropriate for the production code."""
    handler_mapping.append(('/buy_tickets/charge', ChargeWithErrorHandling))
    handler_mapping.append(('/buy_tickets/charge/', ChargeWithErrorHandling))
    return handler_mapping

def create_page_to_dummy_payment(handler_mapping):
    handler_mapping.append(('/buy_tickets/charge', DummyCharge))
    handler_mapping.append(('/buy_tickets/charge/', DummyCharge))
    return handler_mapping
