#!/usr/bin/env python

# Before running
# > source activate py27

#from subprocess import call
#print(call(['source', 'activate', 'py27']))

import os
import sys

sys.path.append('/home/douglas/Dropbox/publicly_visible_binaries/third_party_code_do_not_deploy/google_appengine')
sys.path.append('/home/douglas/Dropbox/publicly_visible_binaries/third_party_code_do_not_deploy/google_appengine/lib/jinja2-2.6')
sys.path.append('/home/douglas/Dropbox/publicly_visible_binaries/third_party_code_do_not_deploy/google_appengine/lib/yaml-3.10')

"""import sys
sys.path.insert(1, 'google-cloud-sdk/platform/google_appengine')
sys.path.insert(1, 'google-cloud-sdk/platform/google_appengine/lib/yaml/lib')
sys.path.insert(1, 'myapp/lib')
"""

#from google.appengine.ext import testbed

from html_generator import process_and_render_html
process_and_render_html.init_template_environment('../html_templates')
