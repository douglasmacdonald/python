#!/usr/bin/env python

import os
import sys

path_to_gae = '/home/douglas/Dropbox/publicly_visible_binaries/third_party_code_do_not_deploy/google_appengine'

sys.path.append(path_to_gae)

#DIR_PATH = os.path.dirname(__file__)

#TEST_LIBRARY_PATHS = [
#    DIR_PATH,
#    os.path.join(DIR_PATH, 'lib', 'cherrypy'),
#]


print sys.path

import wrapper_util

# Before running
# > source activate py27
#import local_lib.local_template_engine as t

# To get the next line to work, it needs the correct relative path.
# The configuration is wrong.
# The configuration could be passed in here
# or the template enginde could be passed in.
# Alternatively move the templates into the processing.
# This makes the templates hard to find but they are closely
# assocoated with the processing
#from html_generator import process_and_render_html
