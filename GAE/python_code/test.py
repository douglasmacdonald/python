#!/usr/bin/env python
"""
This was written with help from web pages
* https://cloud.google.com/appengine/docs/python/tools/localunittesting
* http://einaregilsson.com/unit-testing-model-classes-in-google-app-engine/
"""

################################################################################
import os
import sys
import unittest
################################################################################

################################################################################
sys.path.append('/home/douglas/Dropbox/publicly_visible_binaries/third_party_code_do_not_deploy/google_appengine')
sys.path.append('/home/douglas/Dropbox/publicly_visible_binaries/third_party_code_do_not_deploy/google_appengine/lib/yaml-3.10')
sys.path.append('/home/douglas/Dropbox/publicly_visible_binaries/third_party_code_do_not_deploy/google_appengine/lib/jinja2-2.6')

import wrapper_util
from google.appengine.api import memcache
from google.appengine.ext import testbed
from google.appengine.ext import ndb
################################################################################

class DatastoreTestCase(unittest.TestCase):
    """THE TESTS MUST BE IN THE TEST CLASS. THE CLASS SETUP MANAGES THE GAE
    ENVIRONENT."""

    def setUp(self):

        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()
        # Next, declare which service stubs you want to use.
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        # Clear ndb's in-context cache between tests.
        # This prevents data from leaking between tests.
        # Alternatively, you could disable caching by
        # using ndb.get_context().set_cache_policy(False)
        ndb.get_context().clear_cache()

    def tearDown(self):
        """Datastore teardown."""
        self.testbed.deactivate()
 
    def testT(self):

        from html_generator import process_and_render_html
        
        path_to_templates = '../html_templates'
        process_and_render_html.init_template_environment(path_to_templates)

        from local_lib.local_charge_provider.charge_assume_successful_payment_if_no_error import charge_assume_successful_payment_if_no_error

        from tickets import sold_ticket_list
        sold_ticket_list.append("0", "A", "Not used")
        process_and_render_html.get_buy_tickets_dummy_charge_html({},{}, sold_ticket_list, charge_assume_successful_payment_if_no_error)

    def testT2(self):

        # Have a look at this an possibly change it to
        # sold_ticket_list_database
        # The dot append is confusing becaue sold_ticket_list is
        # a module.
        from tickets import sold_ticket_list
        sold_ticket_list.append("0", "A", "Not used")

    def testT3(self):

        # Okay, what am I going to test html content?
        from html_generator import process_and_render_html
        print process_and_render_html.get_index_page_html("", "")

if __name__ == '__main__':

    unittest.main()
