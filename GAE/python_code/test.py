#!/usr/bin/env python

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
