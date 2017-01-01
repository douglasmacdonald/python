"""
The import of the interfaces is achieved through the __init__.py using *.

The code in this module could (and probably should) be in the __init__.py file.
However, I keep forgetting to look in there.
"""

import sys
import os

# Setting path used for 3rd libraries or my stand alone libraries.
additional_path = os.path.join(sys.path[0], "third_party_code")
sys.path.append(additional_path)

import webapp2 as webapp
import _setup_jinja as template_engine

import damm.damm16 as check_digit_algorithm
import stripe as payment_provider

