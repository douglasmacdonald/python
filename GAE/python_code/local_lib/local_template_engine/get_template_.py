'''The purpose for this is to contain the template environment.

This is about as tight as can be. 

http://jinja.pocoo.org/docs/dev/api/ indicates that it is more normal (if only
using one configuration) to have only on template environment.
'''

from interface import template_engine
import configuration as config
from create_template_environment_ import create_template_environment


template_environment_ = create_template_environment(
    template_engine, config.path_to_templates)

def get_template(template_file_name):

    template = template_environment_.get_template(template_file_name)

    return template
