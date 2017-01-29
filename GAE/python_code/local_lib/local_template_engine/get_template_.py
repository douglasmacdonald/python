'''The purpose for this is to contain the template environment.

This is about as tight as can be. 

http://jinja.pocoo.org/docs/dev/api/ indicates that it is more normal (if only
using one configuration) to have only on template environment.
'''

from interface import template_engine
<<<<<<< Updated upstream
import configuration as config
=======
#import configuration as config
#from configuration import path_to_templates

#from configuration_file import path_to_templates

>>>>>>> Stashed changes
from create_template_environment_ import create_template_environment

template_environment_ = 0

<<<<<<< Updated upstream
template_environment_ = create_template_environment(
    template_engine, config.path_to_templates)
=======
def init_template_environment(path_to_templates):

    #global template_environment_

    global template_environment_
    template_environment_ = create_template_environment(
        template_engine, path_to_templates)
>>>>>>> Stashed changes

def get_template(template_file_name):

    template = template_environment_.get_template(template_file_name)

    return template
