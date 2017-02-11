#!/usr/bin/env python

import os
import sys

#sys.path.append(os.path.join(sys.path[0], '..'))

#sys.path.append(os.path.join(sys.path[0], '..', '..'))

#google_appengine_path = os.path.join(os.path.expanduser("~"), 'Dropbox', 'publicly_visible_binaries', 'third_party_code_do_not_deploy', 'google_appengine')

#sys.path.append(google_appengine_path)

#sys.path.append(os.path.join(google_appengine_path, 'lib', 'jinja2-2.6'))


path_to_templates = '../html_templates'

sys.path.append('/home/douglas/Dropbox/publicly_visible_binaries/third_party_code_do_not_deploy/google_appengine')
sys.path.append('/home/douglas/Dropbox/publicly_visible_binaries/third_party_code_do_not_deploy/google_appengine/lib/jinja2-2.6')
sys.path.append('/home/douglas/Dropbox/publicly_visible_binaries/third_party_code_do_not_deploy/google_appengine/lib/yaml-3.10')

#dir_path = path_to_gae

#os.path.join(dir_path, 'lib', 'jinja2-2.6')

#DIR_PATH = os.path.dirname(__file__)

#TEST_LIBRARY_PATHS = [
#    DIR_PATH,
#    os.path.join(DIR_PATH, 'lib', 'cherrypy'),
#]


#print sys.path

import wrapper_util

# Before running
# > source activate py27


from tickets import sold_ticket_list
import local_lib.local_template_engine as t

# To get the next line to work, it needs the correct relative path.
# The configuration is wrong.
# The configuration could be passed in here
# or the template enginde could be passed in.
# Alternatively move the templates into the processing.
# This makes the templates hard to find but they are closely
# assocoated with the processing
from html_generator import process_and_render_html

#print(dir(process_and_render_html))

path_to_templates = '../html_templates'

process_and_render_html.init_template_environment(path_to_templates)

process_and_render_html.get_index_page_html("", "")

sold_ticket_list.append("0", "A", "Not used")

#process_and_render_html.get_buy_tickets_dummy_charge_html({},{}, sold_ticket_list)

    ##

"""
if __name__ == '__main__':

    import unittest

    class IntegerArithmenticTestCase(unittest.TestCase):
        def testAdd(self):  ## test method names begin 'test*'
            self.assertEqual((1 + 2), 3)
            self.assertEqual(0 + 1, 1)
        def testMultiply(self):
            self.assertEqual((0 * 10), 0)
            self.assertEqual((5 * 8), 40)

    unittest.main()
    """
