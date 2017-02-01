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


print sys.path

import wrapper_util

# Before running
# > source activate py27
import local_lib.local_template_engine as t

# To get the next line to work, it needs the correct relative path.
# The configuration is wrong.
# The configuration could be passed in here
# or the template enginde could be passed in.
# Alternatively move the templates into the processing.
# This makes the templates hard to find but they are closely
# assocoated with the processing
#from html_generator import process_and_render_html
