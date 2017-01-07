"""
The import of the interfaces is achieved through the __init__.py using *.

The code in this module could (and probably should) be in the __init__.py file.
However, I keep forgetting to look in there.
"""

import sys
import os

# Setting path used for 3rd libraries or my stand alone libraries.

additional_path = os.path.join(sys.path[0], "third_party_code")

if additional_path not in sys.path:
     sys.path.insert(0, additional_path)

from damm import damm16 as check_digit_algorithm
