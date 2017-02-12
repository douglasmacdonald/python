#!/usr/bin/env python

# https://cloud.google.com/appengine/docs/python/tools/localunittesting

#http://einaregilsson.com/unit-testing-model-classes-in-google-app-engine/

import unittest

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


class DatastoreTestCase(unittest.TestCase):

    def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()
        # Next, declare which service stubs you want to use.
        self.testbed.init_datastore_v3_stub()
        # Clear ndb's in-context cache between tests.
        # This prevents data from leaking between tests.
        # Alternatively, you could disable caching by
        # using ndb.get_context().set_cache_policy(False)
        ndb.get_context().clear_cache()

    def tearDown(self):
        self.testbed.deactivate()

#sold_ticket_list.append("0", "A", "Not used")
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

from google.appengine.ext import testbed
from google.appengine.ext import ndb
from google.appengine.api import memcache

# [START datastore_example_1]
class TestModel(ndb.Model):
    """A model class used for testing."""
    number = ndb.IntegerProperty(default=42)
    text = ndb.StringProperty()


class TestEntityGroupRoot(ndb.Model):
    """Entity group root"""
    pass


def GetEntityViaMemcache(entity_key):
    """Get entity from memcache if available, from datastore if not."""
    entity = memcache.get(entity_key)
    if entity is not None:
        return entity
    key = ndb.Key(urlsafe=entity_key)
    entity = key.get()
    if entity is not None:
        memcache.set(entity_key, entity)
    return entity
# [END datastore_example_1]


# [START datastore_example_test]
class DatastoreTestCase(unittest.TestCase):

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

# [END datastore_example_test]

    # [START datastore_example_teardown]
    def tearDown(self):
        self.testbed.deactivate()
    # [END datastore_example_teardown]

    # [START datastore_example_insert]
    def testInsertEntity(self):
        TestModel().put()
        self.assertEqual(1, len(TestModel.query().fetch(2)))
    # [END datastore_example_insert]

    # [START datastore_example_filter]
    def testFilterByNumber(self):
        root = TestEntityGroupRoot(id="root")
        TestModel(parent=root.key).put()
        TestModel(number=17, parent=root.key).put()
        query = TestModel.query(ancestor=root.key).filter(
            TestModel.number == 42)
        results = query.fetch(2)
        self.assertEqual(1, len(results))
        self.assertEqual(42, results[0].number)
    # [END datastore_example_filter]

    # [START datastore_example_memcache]
    def testGetEntityViaMemcache(self):
        entity_key = TestModel(number=18).put().urlsafe()
        retrieved_entity = GetEntityViaMemcache(entity_key)
        self.assertNotEqual(None, retrieved_entity)
        self.assertEqual(18, retrieved_entity.number)
    # [END datastore_example_memcache]


# [START main]
if __name__ == '__main__':
    unittest.main()
# [END main]
